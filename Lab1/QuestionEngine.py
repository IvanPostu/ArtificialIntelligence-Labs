import random
from collections import deque
from rules import TOURIST_RULES
from production import (
    IF,
    AND,
    OR,
    NOT,
    instantiate,
    forward_chain,
    backward_chain
)


class QuestionEngine:
    __questions = []
    __questions_dequeue = []
    __tourist_name = None

    def __init__(self, goal_tree, tourist_name):
        self.__tourist_name = tourist_name
        self.__questions = self.__goal_tree_to_questions(goal_tree)
        random.shuffle(self.__questions)
        self.__questions_dequeue = deque(self.__questions)

    @property
    def questions(self):
        return self.__questions

    def get_questions(self):
        result = []
        while len(self.__questions_dequeue) > 0:
            q = None
            if len(self.__questions_dequeue) > 4 and random.randint(1, 2) == 1:
                q = self.__get_question_type2(4)
            else:
                q = self.__get_question_type1()
            if q == None:
                break
            else:
                result.extend(q)
        return result

    def __get_question_type1(self):
        question = self.__questions_dequeue.pop()
        while True:
            try:
                input_string = input(
                    f"\nIs this statement correct? {question} \nEnter (y) if is true, (n) if is false or (x) in order to finish: "
                )

                if input_string.lower() == "x":
                    return None
                if input_string.lower() == "y":
                    return [question]
                if input_string.lower() == "n":
                    return []
                raise ValueError()
            except ValueError:
                print("Error: Input is invalid")

    def __get_question_type2(self, count_of_options):
        result = []
        options = []
        question = f"\nSelect one or more correct options which is true related to {self.__tourist_name} or write (x) in order to finish"

        for i in range(count_of_options):
            options.append(self.__questions_dequeue.pop())
            question += f"\n\t{i+1}) {options[i]}"
        while True:
            input_string = input(
                f"{question}\nEnter a list of space-separated integers: "
            )

            if input_string.lower() == "x":
                return None

            try:
                int_list = list(set([int(x) - 1 for x in input_string.split()]))
                if len(int_list) < 1:
                    raise ValueError()
                for i in int_list:
                    if i >= len(options) or i < 0:
                        raise ValueError()
                for i in int_list:
                    result.append(options[i])
                break
            except ValueError:
                print("Error: Input is invalid")
        return result

    def __goal_tree_to_questions(self, goal_tree):
        result = []
        for node in goal_tree:
            result.extend(self.__node_tree_to_questions(node))

        for i in range(len(result)):
            result[i] = instantiate(result[i], {"x": self.__tourist_name})

        return result

    def __node_tree_to_questions(self, node):
        result = []
        if isinstance(node, IF):
            for rule in node._conditional:
                result.extend(self.__node_tree_to_questions(rule))
        if isinstance(node, AND) or isinstance(node, OR):
            for rule in node:
                result.extend(self.__node_tree_to_questions(rule))
        if isinstance(node, NOT):
            for rule in node:
                result.extend(self.__node_tree_to_questions(rule))
        if isinstance(node, str):
            result.append(node)
        return result


# question_engine = QuestionEngine(TOURIST_RULES, "Jimmy")
# print(question_engine.get_questions())
