import time 

def grap_still(resolve):
    project_manager = resolve.GetProjectManager()
    current_project = project_manager.GetCurrentProject()
    current_timeline = current_project.GetCurrentTimeline()

    markers = current_timeline.GetMarkers()
    start_frame = current_timeline.GetStartFrame()

    raw_fps = current_timeline.GetSetting("timelineFrameRate")
    frame_rate = int(round(float(raw_fps))) 


    def frames_to_timecode(total_frames, fps):
        """Mutlak kare sayısını standart HH:MM:SS:FF timecode string'ine dönüştürür."""
        ff = total_frames % fps
        ss = (total_frames // fps) % 60
        mm = ((total_frames // fps) // 60) % 60
        hh = ((total_frames // fps) // 3600)
        return f"{hh:02d}:{mm:02d}:{ss:02d}:{ff:02d}"


    for rel_frame, marker_data in markers.items():
        if marker_data["color"] == "Red":
            absolute_frame = start_frame + rel_frame
            target_timecode_str = frames_to_timecode(absolute_frame, frame_rate)
            current_timeline.SetCurrentTimecode(target_timecode_str)
            time.sleep(0.2)
            still = current_timeline.GrabStill()
            if still:
                time.sleep(0.2)
                print("resim çekildi galeride")
