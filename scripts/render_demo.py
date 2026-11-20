"""Animate original Petport wireframes as a clearly labeled storyboard."""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw
from image_export import font, save_gif


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    output = args.output or args.root / 'docs/media/petport-journey.gif'
    board = Image.open(args.root / 'wireframe.png').convert('RGB')
    # Crop the two existing application screens, preserving their original content.
    application = board.crop((1266, 50, 1398, 317))
    confirmation = board.crop((1444, 50, 1576, 317))
    screens = [Image.open(args.root/'assets/home.png').convert('RGB'),
               Image.open(args.root/'assets/pet-details.png').convert('RGB'),
               application, confirmation]
    titles = ['Find a companion', 'Review the pet profile', 'Start an application', 'Know what happens next']
    captions = [
        ['Browse the proposed adoption feed.', 'Compare pets and narrow the search.'],
        ['Review available pet information.', 'Move from discovery to a decision.'],
        ['Enter applicant contact details.', 'Keep the next step clear and visible.'],
        ['Show a submission confirmation.', 'Offer a clear route back to browsing.'],
    ]
    stages = []
    for i, screen in enumerate(screens):
        frame = Image.new('RGB', (1000, 660), '#eef5f2')
        d = ImageDraw.Draw(frame)
        d.text((42, 31), 'Petport', font=font(36), fill='#153d36')
        d.rounded_rectangle((43, 89, 356, 122), radius=8, fill='#d8e8e1')
        d.text((56, 97), 'PRODUCT DESIGN / TEAM WIREFRAMES', font=font(14), fill='#235a4b')
        d.text((43, 184), f'0{i+1}', font=font(56), fill='#3b8d75')
        d.text((43, 261), titles[i], font=font(27), fill='#153d36')
        for j, line in enumerate(captions[i]):
            d.text((44, 316+j*32), line, font=font(19), fill='#47645a')
        for j in range(4):
            x = 45 + j*113
            d.rounded_rectangle((x, 439, x+95, 448), radius=4,
                                fill='#3b8d75' if j <= i else '#d2e3da')
            d.text((x, 463), ['Browse','Details','Apply','Confirm'][j],
                   font=font(16), fill='#235a4b' if j == i else '#6a8177')
        d.rounded_rectangle((619, 30, 929, 619), radius=30, fill='#cddfd6')
        d.rounded_rectangle((610, 22, 920, 611), radius=30, fill='#1b3931')
        d.rounded_rectangle((621, 33, 909, 600), radius=22, fill='white')
        screen.thumbnail((270, 535), Image.Resampling.LANCZOS)
        # Existing application crops are lower resolution; enlarge only to the phone panel.
        ratio = min(270/screen.width, 535/screen.height)
        screen = screen.resize((round(screen.width*ratio), round(screen.height*ratio)), Image.Resampling.LANCZOS)
        frame.paste(screen, (765-screen.width//2, 316-screen.height//2))
        d.text((43, 573), 'WIREFRAME STORYBOARD', font=font(17), fill='#235a4b')
        d.text((43, 603), 'Existing design screens; not a running application.', font=font(15), fill='#617a6f')
        stages.append(frame)
    frames, durations = [], []
    for i, stage in enumerate(stages):
        if i:
            for j in range(1, 9):
                frames.append(Image.blend(stages[i-1], stage, j/9))
                durations.append(55)
        frames.append(stage)
        durations.append(2100)
    save_gif(frames, durations, output)


if __name__ == '__main__':
    main()
