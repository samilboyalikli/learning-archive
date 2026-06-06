def add_marker(resolve):
    project_manager = resolve.GetProjectManager()
    current_project = project_manager.GetCurrentProject()
    current_timeline = current_project.GetCurrentTimeline()

    timecode_list = ['01:01:16:22', '01:01:44:06', '01:02:06:06', '01:02:06:19', '01:02:10:04', '01:02:11:03', '01:02:17:20', '01:02:22:08', '01:02:25:06', '01:02:31:19', '01:02:36:04', '01:02:37:23', '01:02:38:01', '01:02:39:02', '01:02:51:23', '01:02:53:02', '01:02:55:00', '01:02:59:24', '01:02:59:24', '01:03:08:20', '01:03:12:17', '01:03:22:19', '01:03:23:19', '01:03:24:02', '01:03:26:08', '01:03:27:11', '01:03:30:24', '01:03:32:07', '01:03:32:09', '01:03:33:16', '01:03:34:03', '01:03:36:14', '01:03:37:15', '01:03:38:07', '01:03:39:01', '01:03:47:10', '01:03:57:04', '01:04:00:13', '01:04:02:14', '01:04:15:03', '01:04:27:00', '01:04:30:21', '01:04:35:24', '01:04:36:09', '01:04:41:00', '01:04:43:13', '01:04:51:02', '01:04:51:21', '01:04:52:14', '01:04:56:10', '01:04:58:00', '01:04:58:14', '01:04:58:16', '01:05:18:06', '01:05:21:09', '01:05:22:02', '01:05:25:05', '01:05:29:13', '01:06:03:00', '01:06:04:09', '01:06:21:11', '01:06:21:16', '01:06:22:03', '01:06:22:21', '01:06:28:14', '01:06:45:02', '01:06:54:16', '01:07:21:02', '01:08:09:00', '01:08:17:19', '01:08:19:16', '01:08:23:13', '01:09:58:07', '01:09:58:18', '01:09:58:19', '01:10:08:18', '01:10:09:10', '01:10:22:05', '01:10:25:18', '01:10:26:03', '01:10:27:17', '01:10:27:17', '01:10:27:19', '01:10:27:21', '01:10:27:23', '01:10:44:23', '01:10:52:19', '01:10:55:03', '01:11:00:04', '01:11:05:17', '01:11:08:04', '01:11:11:16', '01:11:15:02', '01:11:25:17', '01:11:48:05', '01:11:51:10', '01:11:54:12']

    frame_rate = current_timeline.GetSetting("timelineFrameRate")

    def timecode_to_frames(tc, fps):
        """Timecode bilgisini Resolve API'sinin anladığı mutlak kare sayısına (frame) çevirir."""
        parts = list(map(int, tc.split(':')))
        frames = (parts[0] * 3600 + parts[1] * 60 + parts[2]) * int(fps) + parts[3]
        return frames

    start_tc = current_timeline.GetStartFrame()

    for tc in timecode_list:
        try:
            target_frame = timecode_to_frames(tc, frame_rate)
            relative_frame = target_frame - start_tc
            success = current_timeline.AddMarker(
                relative_frame, 
                "Red", 
                "QC_Karesi", 
                f"Otomatik eklenen TC: {tc}", 
                1
            )
            if success:
                print(f"Başarılı: {tc} noktasına kırmızı marker eklendi.")
            else:
                print(f"Başarısız: {tc} için marker eklenemedi (Timeline sınırları dışında olabilir).")
                
        except Exception as e:
            print(f"Hata oluştu ({tc}): {str(e)}")
