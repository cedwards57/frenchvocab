import csv
import random


def quiz(filename):
    with open(filename, newline="") as csvfile:
        reader = csv.reader(csvfile)
        fr_side = []
        en_side = []
        for row in reader:
            fr_side.append(row[0])
            en_side.append(row[1])
    fr_side = list(enumerate(fr_side))
    random.shuffle(fr_side)
    print("Enter the French term. Enter QUIT to stop anytime.")
    for i,answer in fr_side:
        print(en_side[i])
        fr_input = input()
        if(fr_input == "QUIT"):
            break
        print("Your answer: " + fr_input)
        print("True answer: " + answer)
        print("===")


files = {
    "14.1": "vocab_ch14-1_jobs.txt",
    "14.2": "vocab_ch14-2_money.txt",
    "14.3": "vocab_ch14-3_verbs.txt",
    "14.4": "vocab_ch14-4_futursimple.txt",
    "14.5": "vocab_ch14-5_pronomsrelatifs.txt",
    "15.1": "vocab_ch15-1_loisirs.txt",
    "15.2": "vocab_ch15-2_verbs.txt",
    "15.3": "vocab_ch15-3_comparison.txt",
    "15.4": "vocab_ch15-4_questions.txt",
    "15.5": "vocab_ch15-5_conditionnel.txt",
    "16.1": "vocab_ch16-1_subjunctive_conj.txt",
    "16.2": "vocab_ch16-2_subjunctive_expressions.txt",
    "16.3": "vocab_ch16-3_NONsubjunctive_expressions.txt",
    "16.4": "vocab_ch16-4_politics_environment.txt",
}


quiz(files["14.1"])