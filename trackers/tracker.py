from ultralytics import YOLO
import supervision as sv
class Tracker:
    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.tracker = sv.ByteTrack()

    def detect_frames(self,frames):
        batch_size = 20
        detections = []
        for i in range(0,len(frames),batch_size):
            deatections_batch = self.model.track(frames[i:i+batch_size],conf=0.1)
            detections+= deatections_batch
            break

        return detections 
       


    def get_object_tracks(self, frames):
        detections = self.detect_frames(frames)

        for frame_num, detection in enumerate(detection):
            cls_names = detection.names
            cls_names_inv = {v:k for k,v in cls_names.items()}

        #convert to supervision detection format
        detection_supervision = sv.Detections.from_ultralytics(detection)
        print(detection_supervision)