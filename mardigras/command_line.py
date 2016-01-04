import mardigras
import sys
import argparse
from skimage import filter
from skimage.color import rgb2gray
import numpy as np

class MardigrasCmd(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
                description='Runs mardigras commands from console',
                usage='''mardigras <command> [<args>]

edges       applies an edge filter to each frame of a video
flowviz     computes optical flow visualization for all frames (NOT IMPLEMENTED)
''')
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        getattr(self, args.command)()

    def edges(self):
        '''Apply an edge filter to each frame in a video file.'''
        parser = argparse.ArgumentParser(prog='mardigras edges')
        parser.add_argument('inputvideofile', help='the video to apply the edge filter to')
        parser.add_argument('outputvideofile', help='the video to write to')
        parser.add_argument('--method', help='the filtering method', default='sobel', choices=['sobel', 'canny'])
        args = parser.parse_args(sys.argv[2:])
        # define a simple adapter
        def as_rgb(image_filter):
            def rgb_filter(image, *args, **kwargs):
                return image_filter(rgb2gray(image), *args, **kwargs)
            return rgb_filter
        # select filtering method
        if args.method == 'sobel':
            method = as_rgb(filter.sobel)
        elif args.method == 'canny':
            method = as_rgb(filter.canny)
        else:
            exit(1)
        # select output video codec
        codec = 'mp4v' if args.outputvideofile[-4:] == '.mov' else 'h264'
        # filter the video
        mardigras.filter_video(args.inputvideofile, method, args.outputvideofile, codec=codec)

    def flowviz(self):
        '''Compute optical flow visualization for all frames'''
        print('flowviz() not implemented')

def main():
    MardigrasCmd()

if __name__ == '__main__':
    main()
