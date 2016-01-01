import mardigras
import sys
import argparse
from skimage import filter

class MardigrasCmd(object):

    def __init__(self):
        parser = argparse.ArgumentParser(
                description='Runs mardigras commands from console',
                usage='''mardigras <command> [<args>]

edges       applies an edge filter to each frame of a video
flowviz     computes optical flow visualization for all frames
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
        args = parser.parse_args(sys.argv[2:])
        print('called edges()')
        print('reading ' + args.inputvideofile)
        print('writing ' + args.outputvideofile)
        def rgb_sobel(img):
            return filter.sobel(img[:,:,0])**2 + \
                   filter.sobel(img[:,:,1])**2 + \
                   filter.sobel(img[:,:,2])**2
        codec = 'mp4v' if args.outputvideofile[-4:] == '.mov' else 'h264'
        mardigras.filter_video(args.inputvideofile, rgb_sobel, args.outputvideofile, codec=codec)

    def flowviz(self):
        '''Compute optical flow visualization for all frames'''
        print('flowviz() not implemented')

def main():
    MardigrasCmd()

if __name__ == '__main__':
    main()
