from utils import read_video,save_video
from trackers import Tracker

def main():
    source_path = "input_videos/08fd33_4.mp4"
    output_path = "output_videos/output_video.avi"

    # Read video frames
    video_frames, error = read_video(source_path)
    if error:
        print(error)
        return
    
    ##initialize the tracker
    tracker = Tracker('models/best.pt')

    tracks = tracker.get_object_tracks(video_frames)

    # Save video frames to a new file
    try:
        save_video(video_frames, output_path)
        print(f"Video saved to {output_path}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Unexpected error: {str(e)}")


if __name__ == '__main__':
    main()

