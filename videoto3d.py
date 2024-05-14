import numpy as np
import cv2


class Videoto3D:

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def video3d(self, filename, color=False, skip=True):
        cap = cv2.VideoCapture(filename)
        nframe = cap.get(cv2.CAP_PROP_FRAME_COUNT)

        if skip:
            frames = [x * nframe / self.depth for x in range(self.depth)]
        else:
            frames = [x for x in range(self.depth)]

        framearray = []

        try:
            for i in range(self.depth):
                cap.set(cv2.CAP_PROP_POS_FRAMES, frames[i])
                ret, frame = cap.read()

                # Check if frame is valid
                if not ret or frame is None:
                    # Handle empty or invalid frame
                    print(f"Warning: Empty or invalid frame encountered at index {i} in video {filename}")
                    return None

                try:
                    # Resize frame
                    frame = cv2.resize(frame, (self.height, self.width))

                    if color:
                        framearray.append(frame)
                    else:
                        framearray.append(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
                except Exception as e:
                    # Handle any decoding errors
                    print(f"Error decoding frame at index {i} in video {filename}: {e}")
                    return None
        except Exception as e:
            # Handle any other exceptions that may occur during video processing
            print(f"Error processing video {filename}: {e}")
            return None
        finally:
            cap.release()

        return np.array(framearray)


    def get_UCF_classname(self, filename):
        x =  filename[filename.find('_') + 1:filename.find('_', 1)]
        print(x)
        return x