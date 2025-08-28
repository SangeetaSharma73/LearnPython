import cv2
import mediapipe as mp
import math
import numpy as np
import time

class RealTimeYogaPoseDetector:
    def __init__(self):
        # Initialize MediaPipe pose detection
        self.mp_pose = mp.solutions.pose
        self.mp_drawing = mp.solutions.drawing_utils
        
        # Set up pose detection for video (not static images)
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,  # Set to False for video processing
            min_detection_confidence=0.7,  # Higher confidence for better accuracy
            min_tracking_confidence=0.5,
            model_complexity=1  # Lower complexity for better real-time performance
        )
        
        # Initialize webcam
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        
        # Pose tracking variables
        self.current_pose = "Unknown Pose"
        self.pose_confidence = 0.0
        self.pose_start_time = None
        self.pose_hold_duration = 0.0
        
    def calculate_angle(self, landmark1, landmark2, landmark3):
        """Calculate angle between three landmarks"""
        x1, y1, _ = landmark1
        x2, y2, _ = landmark2
        x3, y3, _ = landmark3
        
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        
        if angle < 0:
            angle += 360
            
        return angle
    
    def calculate_pose_accuracy(self, landmarks, pose_name):
        """Calculate accuracy score for detected pose based on ideal angles"""
        if not landmarks or len(landmarks) < 33:
            return 0.0
            
        # Calculate joint angles
        left_elbow_angle = self.calculate_angle(
            landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value],
            landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value],
            landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST.value]
        )
        
        right_elbow_angle = self.calculate_angle(
            landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
            landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value],
            landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value]
        )
        
        left_shoulder_angle = self.calculate_angle(
            landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value],
            landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value],
            landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value]
        )
        
        right_shoulder_angle = self.calculate_angle(
            landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value],
            landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
            landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value]
        )
        
        left_knee_angle = self.calculate_angle(
            landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value],
            landmarks[self.mp_pose.PoseLandmark.LEFT_KNEE.value],
            landmarks[self.mp_pose.PoseLandmark.LEFT_ANKLE.value]
        )
        
        right_knee_angle = self.calculate_angle(
            landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value],
            landmarks[self.mp_pose.PoseLandmark.RIGHT_KNEE.value],
            landmarks[self.mp_pose.PoseLandmark.RIGHT_ANKLE.value]
        )
        
        def calculate_angle_accuracy(actual_angle, ideal_angle, tolerance=30):
            """Calculate accuracy for a single angle with gradual scoring"""
            angle_diff = abs(actual_angle - ideal_angle)
            # Handle angle wraparound (e.g., 350° vs 10°)
            angle_diff = min(angle_diff, 360 - angle_diff)
            
            if angle_diff <= tolerance:
                # Linear decrease from 100% to 60% within tolerance
                return max(0.6, 1.0 - (angle_diff / tolerance) * 0.4)
            else:
                # Exponential decrease beyond tolerance
                excess = angle_diff - tolerance
                return max(0.0, 0.6 * math.exp(-excess / 20))
        
        accuracy_scores = []
        
        if pose_name == "Warrior II Pose":
            # Ideal angles for Warrior II with more forgiving tolerances
            left_elbow_acc = calculate_angle_accuracy(left_elbow_angle, 180, 25)
            right_elbow_acc = calculate_angle_accuracy(right_elbow_angle, 180, 25)
            left_shoulder_acc = calculate_angle_accuracy(left_shoulder_angle, 90, 20)
            right_shoulder_acc = calculate_angle_accuracy(right_shoulder_angle, 90, 20)
            
            # Check for warrior stance (one leg bent, one straight)
            left_knee_acc = max(
                calculate_angle_accuracy(left_knee_angle, 105, 25),  # Bent leg
                calculate_angle_accuracy(left_knee_angle, 180, 15)   # Straight leg
            )
            right_knee_acc = max(
                calculate_angle_accuracy(right_knee_angle, 105, 25), # Bent leg
                calculate_angle_accuracy(right_knee_angle, 180, 15)  # Straight leg
            )
            
            accuracy_scores = [left_elbow_acc, right_elbow_acc, left_shoulder_acc, 
                             right_shoulder_acc, left_knee_acc, right_knee_acc]
            
        elif pose_name == "T Pose":
            # Ideal angles for T Pose
            left_elbow_acc = calculate_angle_accuracy(left_elbow_angle, 180, 20)
            right_elbow_acc = calculate_angle_accuracy(right_elbow_angle, 180, 20)
            left_shoulder_acc = calculate_angle_accuracy(left_shoulder_angle, 90, 15)
            right_shoulder_acc = calculate_angle_accuracy(right_shoulder_angle, 90, 15)
            left_knee_acc = calculate_angle_accuracy(left_knee_angle, 180, 15)
            right_knee_acc = calculate_angle_accuracy(right_knee_angle, 180, 15)
            
            accuracy_scores = [left_elbow_acc, right_elbow_acc, left_shoulder_acc, 
                             right_shoulder_acc, left_knee_acc, right_knee_acc]
            
        elif pose_name == "Tree Pose":
            # Tree pose: one leg straight, one leg bent and raised
            straight_leg_acc = max(
                calculate_angle_accuracy(left_knee_angle, 180, 15),
                calculate_angle_accuracy(right_knee_angle, 180, 15)
            )
            
            # Check for bent leg (should be around 45-90 degrees)
            bent_leg_acc = max(
                calculate_angle_accuracy(left_knee_angle, 45, 30) if left_knee_angle < 120 else 0,
                calculate_angle_accuracy(right_knee_angle, 45, 30) if right_knee_angle < 120 else 0
            )
            
            # Balance component (arms can be in various positions)
            arm_balance_acc = (calculate_angle_accuracy(left_elbow_angle, 180, 40) + 
                             calculate_angle_accuracy(right_elbow_angle, 180, 40)) / 2
            
            accuracy_scores = [straight_leg_acc, bent_leg_acc, arm_balance_acc]
        
        # Return weighted average accuracy
        if accuracy_scores:
            return sum(accuracy_scores) / len(accuracy_scores)
        else:
            return 0.0
    
    def classify_pose(self, landmarks, output_image):
        """Classify yoga pose and return pose name with confidence"""
        if not landmarks or len(landmarks) < 33:
            return output_image, "Unknown Pose", 0.0
            
        label = 'Unknown Pose'
        color = (0, 0, 255)  # Red for unknown
        
        # Calculate angles (same logic as original)
        left_elbow_angle = self.calculate_angle(
            landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value],
            landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value],
            landmarks[self.mp_pose.PoseLandmark.LEFT_WRIST.value]
        )
        
        right_elbow_angle = self.calculate_angle(
            landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
            landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value],
            landmarks[self.mp_pose.PoseLandmark.RIGHT_WRIST.value]
        )
        
        left_shoulder_angle = self.calculate_angle(
            landmarks[self.mp_pose.PoseLandmark.LEFT_ELBOW.value],
            landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER.value],
            landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value]
        )
        
        right_shoulder_angle = self.calculate_angle(
            landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value],
            landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER.value],
            landmarks[self.mp_pose.PoseLandmark.RIGHT_ELBOW.value]
        )
        
        left_knee_angle = self.calculate_angle(
            landmarks[self.mp_pose.PoseLandmark.LEFT_HIP.value],
            landmarks[self.mp_pose.PoseLandmark.LEFT_KNEE.value],
            landmarks[self.mp_pose.PoseLandmark.LEFT_ANKLE.value]
        )
        
        right_knee_angle = self.calculate_angle(
            landmarks[self.mp_pose.PoseLandmark.RIGHT_HIP.value],
            landmarks[self.mp_pose.PoseLandmark.RIGHT_KNEE.value],
            landmarks[self.mp_pose.PoseLandmark.RIGHT_ANKLE.value]
        )
        
        # Pose classification logic (same as original)
        if left_elbow_angle > 165 and left_elbow_angle < 195 and right_elbow_angle > 165 and right_elbow_angle < 195:
            if left_shoulder_angle > 80 and left_shoulder_angle < 110 and right_shoulder_angle > 80 and right_shoulder_angle < 110:
                if left_knee_angle > 165 and left_knee_angle < 195 or right_knee_angle > 165 and right_knee_angle < 195:
                    if left_knee_angle > 90 and left_knee_angle < 120 or right_knee_angle > 90 and right_knee_angle < 120:
                        label = 'Warrior II Pose'
                        
                if left_knee_angle > 160 and left_knee_angle < 195 and right_knee_angle > 160 and right_knee_angle < 195:
                    label = 'T Pose'
        
        if left_knee_angle > 165 and left_knee_angle < 195 or right_knee_angle > 165 and right_knee_angle < 195:
            if left_knee_angle > 315 and left_knee_angle < 335 or right_knee_angle > 25 and right_knee_angle < 45:
                label = 'Tree Pose'
        
        # Calculate accuracy for detected pose
        accuracy = self.calculate_pose_accuracy(landmarks, label) if label != 'Unknown Pose' else 0.0
        
        if label != 'Unknown Pose':
            color = (0, 255, 0)  # Green for detected poses
            
        return output_image, label, accuracy
    
    def detect_pose(self, image):
        """Detect pose landmarks in image"""
        output_image = image.copy()
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        results = self.pose.process(imageRGB)
        
        height, width, _ = image.shape
        landmarks = []
        
        if results.pose_landmarks:
            # Draw pose landmarks
            self.mp_drawing.draw_landmarks(
                image=output_image, 
                landmark_list=results.pose_landmarks,
                connections=self.mp_pose.POSE_CONNECTIONS,
                landmark_drawing_spec=self.mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2),
                connection_drawing_spec=self.mp_drawing.DrawingSpec(color=(255,255,255), thickness=2)
            )
            
            # Extract landmark coordinates
            for landmark in results.pose_landmarks.landmark:
                landmarks.append((
                    int(landmark.x * width), 
                    int(landmark.y * height),
                    landmark.z * width
                ))
                
        return output_image, landmarks
    
    def run(self):
        """Main loop for real-time pose detection"""
        print("Starting Real-Time Yoga Pose Detector...")
        print("Press 'q' to quit, 'r' to reset pose timer")
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to grab frame")
                break
                
            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)
            
            # Detect pose
            output_image, landmarks = self.detect_pose(frame)
            
            # Classify pose
            output_image, pose_name, accuracy = self.classify_pose(landmarks, output_image)
            
            current_time = time.time()
            if pose_name != "Unknown Pose":
                if self.current_pose != pose_name:
                    self.current_pose = pose_name
                    self.pose_start_time = current_time
                    self.pose_hold_duration = 0.0
                else:
                    if self.pose_start_time:
                        self.pose_hold_duration = current_time - self.pose_start_time
                        
                self.pose_confidence = min(1.0, accuracy + (self.pose_hold_duration * 0.1))
            else:
                self.current_pose = "Unknown Pose"
                self.pose_confidence = 0.0
                self.pose_start_time = None
                self.pose_hold_duration = 0.0
            
            # Background for text
            cv2.rectangle(output_image, (10, 10), (600, 120), (0, 0, 0), -1)
            cv2.rectangle(output_image, (10, 10), (600, 120), (255, 255, 255), 2)
            
            # Pose name
            color = (0, 255, 0) if pose_name != "Unknown Pose" else (0, 0, 255)
            cv2.putText(output_image, f"Pose: {pose_name}", (20, 40), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            
            # Accuracy percentage
            accuracy_percent = int(self.pose_confidence * 100)
            cv2.putText(output_image, f"Accuracy: {accuracy_percent}%", (20, 70), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            # Hold duration
            cv2.putText(output_image, f"Hold Time: {self.pose_hold_duration:.1f}s", (20, 100), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            # Accuracy bar
            bar_width = int(400 * self.pose_confidence)
            cv2.rectangle(output_image, (20, 130), (420, 150), (100, 100, 100), -1)
            cv2.rectangle(output_image, (20, 130), (20 + bar_width, 150), (0, 255, 0), -1)
            cv2.rectangle(output_image, (20, 130), (420, 150), (255, 255, 255), 2)
            
            # Instructions
            cv2.putText(output_image, "Press 'q' to quit, 'r' to reset timer", 
                       (20, output_image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            
            # Display the frame
            cv2.imshow('Real-Time Yoga Pose Detector', output_image)
            
            # Handle key presses
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('r'):
                self.pose_start_time = current_time
                self.pose_hold_duration = 0.0
                print("Pose timer reset!")
                
        # Cleanup
        self.cap.release()
        cv2.destroyAllWindows()
        print("Real-time yoga pose detector stopped.")

if __name__ == "__main__":
    detector = RealTimeYogaPoseDetector()
    detector.run()
