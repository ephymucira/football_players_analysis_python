import cv2
import os

import cv2
import os

# def read_video(source_path):
#     # Check for empty file path
#     if not source_path:
#         return None, "Error: Empty file path provided"

#     frames = []
#     try:
#         # Check if the video file exists
#         if os.path.exists(source_path):
#             cap = cv2.VideoCapture(source_path)
#             if not cap.isOpened():
#                 return None, f"Error: Could not open video file: {source_path}"
            
#             # Read frames from the video
#             while True:
#                 ret, frame = cap.read()
#                 if not ret:
#                     break
#                 if frame is not None:  # Only append valid frames
#                     frames.append(frame)
            
#             cap.release()
#             if not frames:  # If no valid frames are captured
#                 return None, "Error: No valid frames read from the video."
#             return frames, None
#         else:
#             return None, f"Error: File does not exist: {source_path}"
#     except Exception as e:
#         return None, f"Error: {str(e)}"

def read_video(source_path):
    # Check for empty file path
    if not source_path:
        return None, "Error: Empty file path provided"

    frames = []
    try:
        # Check if the video file exists
        if os.path.exists(source_path):
            cap = cv2.VideoCapture(source_path)
            if not cap.isOpened():
                return None, f"Error: Could not open video file: {source_path}"
            
            frame_index = 0
            # Read frames from the video
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                if frame is not None:
                    frames.append(frame)
                else:
                    print(f"Warning: Frame at index {frame_index} is None and will be skipped.")
                frame_index += 1
            
            cap.release()
            if not frames:  # If no valid frames are captured
                return None, "Error: No valid frames read from the video."
            return frames, None
        else:
            return None, f"Error: File does not exist: {source_path}"
    except Exception as e:
        return None, f"Error: {str(e)}"




# def save_video(output_video_frames, output_video_path):
#     if not output_video_frames:
#         raise ValueError("Error: No frames to save in the video.")

#     # Check if all frames are valid
#     for i, frame in enumerate(output_video_frames):
#         if frame is None:
#             raise ValueError(f"Error: Frame at index {i} is invalid (None).")

#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     height, width = output_video_frames[0].shape[:2]
#     out = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height))

#     for frame in output_video_frames:
#         out.write(frame)

#     out.release()



# def save_video(output_video_frames, output_video_path):
#     if not output_video_frames:
#         raise ValueError("Error: No frames to save in the video.")

#     fourcc = cv2.VideoWriter_fourcc(*'XVID')
#     height, width = output_video_frames[0].shape[:2]
#     out = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height))

#     for frame in output_video_frames:
#         out.write(frame)

#     out.release()

def save_video(output_video_frames, output_video_path):
    # Ensure there are valid frames
    valid_frames = [frame for frame in output_video_frames if frame is not None]
    if not valid_frames:
        raise ValueError("Error: No valid frames to save in the video.")

    print(f"Debug: Number of valid frames to save = {len(valid_frames)}")

    # Get dimensions from the first valid frame
    height, width = valid_frames[0].shape[:2]
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (width, height))

    # Write valid frames
    for frame in valid_frames:
        out.write(frame)

    out.release()
    print(f"Debug: Video successfully saved to {output_video_path}")


