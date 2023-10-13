import argparse
import os
import src.constants as cons
import src.results.results as res
import src.results.scores as scores
import src.results.post_process as pp

# Adiciona os argumentos
parser = argparse.ArgumentParser(description='Prepare the data for training, splitting it into train and test sets and augmenting it.')

parser.add_argument('--n', type=str, default="2", help='Number of pairs to visualize')
parser.add_argument('--overlay', type=bool, default=False, help='Overlay the masks on the images when visualizing')
parser.add_argument('--visualizeR', choices=['result1', 'result2'], help='Visualize the pairs in the splits, can change the number of pairs to visualize using --n argument')
parser.add_argument('--visualizeP', action='store_true', help='Visualize the pairs in the splits, can change the number of pairs to visualize using --n argument')
parser.add_argument('--noshuffle', action='store_false', default=True, help='Set this flag to not shuffle the images when visualizing')
parser.add_argument('--visualizeRx', choices=['result1', 'result2'], help='Visualize the specified result ussing the --n argument')
parser.add_argument('--score', choices=['all', 'dice', 'iou'], help='Calculate the specified score for the specified result ussing the --n argument')
parser.add_argument('--pp', action='store_true', help='Post process the masks')

# Analisa os argumentos
args = parser.parse_args()

# Get the value of arg.n if it is not None
if args.n:
    if not args.n  == "all":
        args.n = int(args.n)
    else:
        assert args.n == "all", "Invalid value for --n argument"

# Visualiza os resultados se o argumento --visualizeResult foi fornecido
if args.visualizeR:
    print("\n ### Visualizing result ################################## \n")
    if args.visualizeR == 'result1':
        res.overlay_with_bounding_box(cons.RESULT_DIR, args.n, args.overlay, 1, args.noshuffle)
    elif args.visualizeR == 'result2':
        res.overlay_with_bounding_box(cons.RESULT_DIR, args.n, args.overlay, 2, args.noshuffle)

# Visualiza os pares se o argumento --visualizepairs foi fornecido
elif args.visualizeP:
    print("\n ### Visualizing pairs ################################## \n")
    res.visualize_all(args.n, args.overlay, args.noshuffle)

# Visualiza o resultado especificado pelo argumento --visualizeRx
elif args.visualizeRx:
    print("\n ### Visualizing result ################################## \n")
    if args.visualizeRx == 'result1':
        res.overlay_with_bounding_box_specific(cons.RESULT_DIR, args.n, args.overlay, 1, args.noshuffle)
    elif args.visualizeRx == 'result2':
        res.overlay_with_bounding_box_specific(cons.RESULT_DIR, args.n, args.overlay, 2, args.noshuffle)

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
    pp.aumentar_brilho(os.path.join(cons.RESULT_DIR, 'result002' ,'pp', 'SRM_052_0000.png'), 1.5)
