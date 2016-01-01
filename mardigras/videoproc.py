import cv2
import numpy as np

def filter_video(inputvideofile, func, outputvideofile, codec='h264'):
    print('called filter_video()')
    # open input video file
    reader = cv2.VideoCapture(inputvideofile)
    # process the first frame to set image size and levels
    retval,frame = reader.read()
    assert(retval)  # there must be at least one frame
    processed_frame = func(frame)
    reader.release()
    assert(processed_frame.ndim <= 3)  # output must be grayscale or RGB
    # check if the processed frame has negative values
    if (processed_frame < 0).any():
        # gray value 127 = 0
        origin = 127.0
        # rescale such that all values fit in 0-255
        scale = 127.0 / max(abs(processed_frame.min()), abs(processed_frame.max()))
    else:
        origin = 0.0
        # rescale such that all values fit in 0-255
        scale = 255.0 / (np.percentile(processed_frame.flatten(),98))
    # check if processed frame is grayscale or RGB
    grayscale = False
    if processed_frame.ndim == 2 or processed_frame.shape[2] == 1:
        grayscale = True
    # output settings
    fps = 24
    height, width = processed_frame.shape[0:2]
    fourcc = cv2.VideoWriter_fourcc(*codec)
    # open intput video file
    reader = cv2.VideoCapture(inputvideofile)
    # open output video file
    vout = cv2.VideoWriter()
    success = vout.open(outputvideofile,fourcc,fps,(width,height),True)
    if not success:
        print('Could not open ' + outputvideofile + ' for writing')
        return False
    # process all frames
    while True:
        retval,frame = reader.read()
        # check if frames have all been read
        if not retval:
            break
        # process frame
        processed_frame = func(frame)
        # if grayscale, convert to RGB
        if grayscale:
            processed_frame = processed_frame.reshape((height,width,1)).repeat(3,axis=2)
        # rescale pixel values and clip
        processed_frame = (scale * processed_frame) + origin
        np.clip(processed_frame, 0, 255, out=processed_frame)
        # write to output video
        vout.write(processed_frame.astype(np.uint8))
    # clean up
    vout.release()
    reader.release()
