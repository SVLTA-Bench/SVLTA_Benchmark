import argparse

from generate_videos import generate_all_videos
from generate_queries import generate_all_queries
from generate_timestamps import generate_all_timestamps


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max_num_actions', type=int, default=4, help='[4, 5, 6, 7, 8, 9, 10, 11, 12]')
    parser.add_argument('--type', type=str, help='[video, query, timestamp]')
    parser.add_argument('--max_iteration', type=int, default=500, help='max iteration')
    parser.add_argument('restart', type=bool, default=True, help='whether start from break point')
    parser.add_argument('--all_actions_file', type=str, default="./data/all_actions.json", help='all actions')
    parser.add_argument('--rooms', type=list, default=["livingroom", "kitchen", "bedroom", "bathroom"], help='all rooms')
    parser.add_argument('--characters', type=list, default=["Male1", "Female1", "Female2", "Female4", "Male10", "Male2"], help='all agents')
    parser.add_argument('--all_scene_ids_file', type=str, default="./data/scene_ids.json", help='all situations ids')
    parser.add_argument('--input_path', type=str, default="./data/frames", help='input frames path')
    parser.add_argument('--output_path', type=str, default="./data/videos", help='output videos path')
    parser.add_argument('--memory_scripts_scenes_actions_file', type=str, default="./data/memory_scripts_scenes_actions.json", help='save scripts scenes actions')
    parser.add_argument('--memory_scripts_scenes_actions_queries_file', type=str, default="./data/memory_scripts_scenes_actions_queries.json", help='save scripts scenes actions queries')
    args = parser.parse_args()

    return args

def main():
    args = parse_args()
    if args.type == "video":
        generate_all_videos(args)
    elif args.type == "query":
        generate_all_queries(args)
    elif args.type == "timestamp":
        generate_all_timestamps(args)
    else:
        raise ValueError("Unknown type {}!!!".format(args.type))

if __name__ == "__main__":
    main()