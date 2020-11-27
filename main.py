import argparse
import textwrap
import Org_ext
import Org_size
import Org_month


def main():

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(
            """
                        Please choose any of the followig commands !!
        ----------------------------------------------------------------------------
        Organize by extesion                   : python fileName.py --org ext
        Organize by size                       : python fileName.py --org size
        Organize by month                      : python fileName.py --org month
        Organize a folder by user defined path : python fileName.py --path  "path"
        """
        ),
    )

    parser.add_argument('--path', default='.',
                        help='Absolute path of the directory to be Organised'
                        )

    parser.add_argument('--org', default='ext', choices=['ext', 'size',
                        'month'], help='These functons can be done.')

    args = parser.parse_args()
    path = args.path
    if args.org == 'ext':
        Org_ext.Organize_ext(path)
    elif args.org == 'size':
        Org_size.Organize_size(path)
    elif args.org == 'month':
        Org_month.Organize_month(path)


if __name__ == '__main__':

    main()
