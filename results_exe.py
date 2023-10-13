import argparse
import os
import src.constants as cons
import src.results.results as res
import src.results.scores as scores
import src.results.post_process as pp

# Adiciona os argumentos
parser = argparse.ArgumentParser(description='Prepare the data for training, splitting it into train and test sets and augmenting it.')

parser.add_argument('--visualizeP', action='store_true', help='Visualize the result pairs, can change the number of pairs to visualize using --n argument'
                    'use --nosuffle to not shuffle the images when visualizing')
parser.add_argument('--visualizePx', action='store_true', help='Visualize the specified result the --n argument'
                    'use --nosuffle to not shuffle the images when visualizing')
parser.add_argument('--visualizeR', action='store_true', help='Visualize the bonding box of the results, '
                    'can change the number of results displayed using --n argument'
                    'use --nosuffle to not shuffle the images when visualizing'
                    'use --noverlay to not overlay the masks on the images when visualizing')
parser.add_argument('--visualizeRx', action='store_true', help='Visualize the bonding box of the specific result, '
                    'can change the number of results displayed using --n argument'
                    'use --nosuffle to not shuffle the images when visualizing'
                    'use --noverlay to not overlay the masks on the images when visualizing')
parser.add_argument('--score', choices=['all', 'dice', 'iou'], help='Calculate the specified score for the specified result ussing the --n argument'
                    'use "--n" to specify the number of the image to calculate the score for or "--n all" to calculate the score for all images (mean)')
parser.add_argument('--noverlay', type=bool, default=True, help='Overlay the masks on the images when visualizing')
parser.add_argument('--noshuffle', action='store_false', default=True, help='Set this flag to not shuffle the images when visualizing')
parser.add_argument('--n', type=str, default="2", help='Used with --visualizeP, --visualizeR, --visualizeRx, --score.'
                    'Specify the number of images to visualize or the number of the image to visualize'
                    'Can be "all" to visualize all images')
parser.add_argument('--pp', action='store_true', help='Post process the masks')

# Analisa os argumentos
args = parser.parse_args()

# Get the value of arg.n if it is not None
if args.n:
    if not args.n  == "all":
        assert int(args.n) >= 0 and int(args.n) <= 100, "Invalid value for --n argument"
    else:
        assert args.n == "all", "Invalid value for --n argument"

# Visualiza os pares se o argumento --visualizepairs foi fornecido
elif args.visualizeP:
    print("\n ### Visualizing pairs ################################## \n")
    res.visualize_all(args.n, args.noshuffle)

# Visualiza o resultado especificado pelo argumento --visualizePx
elif args.visualizePx:
    print("\n ### Visualizing result ################################## \n")
    res.visualize_all_specific(args.n)

# Visualiza os resultados se o argumento --visualizeResult foi fornecido
if args.visualizeR:
    print("\n ### Visualizing result ################################## \n")
    res.overlay_with_bounding_box(args.n, args.noverlay, args.noshuffle)

# Visualiza o resultado especificado pelo argumento --visualizeRx
elif args.visualizeRx:
    print("\n ### Visualizing result ################################## \n")
    res.overlay_with_bounding_box_specific(args.n, args.noverlay, args.noshuffle)

# Calcula o score especificado pelo argumento --score
elif args.score:
    print("\n ### Calculating score ################################## \n")
    if args.score == 'all':
        scores.calculate_score(args.n, 2)
    elif args.score == 'dice':
        scores.calculate_score(args.n, 1)
    elif args.score == 'iou':
        scores.calculate_score(args.n, 0)

# Post processa 
if args.pp:
    print("\n ### Post processing ################################## \n")
    pp.change_intensity(os.path.join(cons.RESULT_DIR, 'result002' ,'pp', 'SRM_052_0000.png'), 1.5)
