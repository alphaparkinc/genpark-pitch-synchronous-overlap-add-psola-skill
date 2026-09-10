class TDPSOLA:
    """
    Time-Domain Pitch-Synchronous Overlap-Add (TD-PSOLA).
    Modifies audio timescale / playback speed without altering pitch.
    """
    def time_stretch(self, signal, pitch_period, stretch_factor=1.5):
        output = []
        for i in range(0, len(signal) - pitch_period, pitch_period):
            frame = signal[i:i+pitch_period]
            output.extend(frame)
            if stretch_factor > 1.0:
                dup_count = int(stretch_factor) - 1
                for _ in range(dup_count):
                    output.extend(frame)
        return output
