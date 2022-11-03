import sys
import csv


def main():
    if len(sys.argv) != 3:
        print("\nCOLLECTION TO DECK UTILITY")
        print(
            "Translates an exported Collection .csv file from Archidekt.com into a .txt file that may be imported as a Deck"
        )
        print("USAGE:")
        print(sys.argv[0] + " path_to_csv_input path_to_txt_output\n")

    else:
        collection_to_deck()
        print("\nSuccesfully created deck txt file in " + sys.argv[1] + "\n")


def collection_to_deck():
    with open(sys.argv[1]) as csv_in:
        rd = csv.DictReader(csv_in)
        with open(sys.argv[2], "w") as txt_out:
            for rw in rd:
                txt_out.write(
                    rw["Quantity"]
                    + "x "
                    + rw["Name"]
                    + " ("
                    + rw["Edition Code"]
                    + ")\n"
                )


main()
