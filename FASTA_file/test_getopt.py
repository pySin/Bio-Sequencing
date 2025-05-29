import sys
import getopt

def main(argv):
    # Default values
    input_file = ""
    output_file = ""
    verbose = False
    mode = "default"

    all_args = getopt.getopt(
        argv,  # Arguments passed to the script
        # "hi:o:v",                       # Short options (`h` for help, `i:` expects a value)
        "i:z:m:l:s",
        ["help", "input=", "output=", "verbose", "mode="]  # Long options
    )
    print(f"All args: {all_args}")

    # try:
    #     # Define short and long options
    #     opts, args = getopt.getopt(
    #         argv,                           # Arguments passed to the script
    #         #"hi:o:v",                       # Short options (`h` for help, `i:` expects a value)
    #         "o",
    #         ["help", "input=", "output=", "verbose", "mode="]  # Long options
    #     )
    # except getopt.GetoptError as e:
    #     print(f"Error: {e}")
    #     sys.exit(2)
    #
    # print(f"Optionals: {opts}")
    # print(f"Required: {args}")
    #
    # # Process options
    # for opt, arg in opts:
    #     if opt in ("-h", "--help"):
    #         print("Usage: script.py -i <input> -o <output> --verbose --mode=<mode>")
    #         sys.exit()
    #     elif opt in ("-i", "--input"):
    #         input_file = arg
    #     elif opt in ("-o", "--output"):
    #         output_file = arg
    #     elif opt in ("-v", "--verbose"):
    #         verbose = True
    #     elif opt == "--mode":
    #         mode = arg
    #
    # print(f"Input: {input_file}, Output: {output_file}, Verbose: {verbose}, Mode: {mode}")

if __name__ == "__main__":
    main(sys.argv[1:])  # Skip the script name (first argument)