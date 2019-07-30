from datetime import datetime

# request body data validation
import typing
import pydantic
from pydantic.dataclasses import dataclass


@dataclass
class HandshakeQuestionCategory:
    name: str


@dataclass
class HandshakeQuestionSpectrum:
    name: str
    direction: HandshakeQuestionCategory


@dataclass
class HandshakeQuestion:
    category: HandshakeQuestionCategory
    text: str


@dataclass
class HandshakeAnswer:
    question: HandshakeQuestion
    response: int

    @pydantic.validator('response')
    def must_be_1_through_5(cls, response):
        if not 1 <= response <= 5:
            raise ValueError('Handshake response must be 1 through 5 inclusive.')
        return response


@dataclass
class HandshakeResponse:
    user_id: int = None
    answers: typing.List[HandshakeAnswer]

    @pydantic.validator('answers')
    def must_correspond_to_handshake_definition(cls, answers):
        for answer, question in zip(answers, HANDSHAKE):
            if answer != question:
                raise ValueError('Handshake answers not matching handshake definition.')
        return answers


ACTIVE = HandshakeQuestionSpectrum(name="Factual", direction=HandshakeQuestionCategory(name="Active"))
REFLECTIVE = HandshakeQuestionSpectrum(name="Factual", direction=HandshakeQuestionCategory(name="Reflective"))
SENSING = HandshakeQuestionSpectrum(name="Conceptual", direction=HandshakeQuestionCategory(name="Sensing"))
INTUITIVE = HandshakeQuestionSpectrum(name="Conceptual", direction=HandshakeQuestionCategory(name="Intuitive"))
VISUAL = HandshakeQuestionSpectrum(name="Procedure", direction=HandshakeQuestionCategory(name="Visual"))
VERBAL = HandshakeQuestionSpectrum(name="Procedure", direction=HandshakeQuestionCategory(name="Verbal"))
SEQUENTIAL = HandshakeQuestionSpectrum(name="Analytical", direction=HandshakeQuestionCategory(name="Sequential"))
GLOBAL = HandshakeQuestionSpectrum(name="Analytical", direction=HandshakeQuestionCategory(name="Global"))
SELF_PERCEPTION = HandshakeQuestionCategory(name="Self-Perception")


@dataclass
class HandshakeType:
    name: str
    questions: typing.List[HandshakeQuestion]


HANDSHAKE = HandshakeType(name="Handshake0", questions=[
    HandshakeQuestion(category=ACTIVE,
                      text="When I start a homework problem, I am more likely to start working on the solution immediately."),
    HandshakeQuestion(category=ACTIVE,
                      text="I am more likely to be considered outgoing."),
    HandshakeQuestion(category=ACTIVE,
                      text="I more easily remember something I have done."),
    HandshakeQuestion(category=ACTIVE,
                      text="In a study group working on difficult material, I am likely to jump in a contribute ideas."),
    HandshakeQuestion(category=ACTIVE,
                      text="When I am learning something new, it helps me to talk about it."),
    HandshakeQuestion(category=REFLECTIVE,
                      text="When I start a homework problem, I am more likely to try to fully understand the problem set."),
    HandshakeQuestion(category=REFLECTIVE,
                      text="I am more likely to be considered reserved."),
    HandshakeQuestion(category=REFLECTIVE,
                      text="I more easily remember something I have thought a lot about."),
    HandshakeQuestion(category=REFLECTIVE,
                      text="In a study group working on difficult material, I am likely to sit back and listen."),
    HandshakeQuestion(category=REFLECTIVE,
                      text="When I am learning something new, it helps me to think about it."),
    HandshakeQuestion(category=SENSING,
                      text="When I am reading for enjoyment, I like writers to clearly say what they mean."),
    HandshakeQuestion(category=SENSING,
                      text="I consider it higher praise to call someone sensible."),
    HandshakeQuestion(category=SENSING,
                      text="I would rather be considered realistic."),
    HandshakeQuestion(category=SENSING,
                      text="I find it easier to learn facts."),
    HandshakeQuestion(category=SENSING,
                      text="If I were a teacher, I would rather teach a course that deals with facts and real life situations."),
    HandshakeQuestion(category=INTUITIVE,
                      text="When I am reading for enjoyment, I like writers to say things in creative, interesting ways."),
    HandshakeQuestion(category=INTUITIVE,
                      text="I consider it higher praise to call someone imaginative."),
    HandshakeQuestion(category=INTUITIVE,
                      text="I would rather be considered innovative."),
    HandshakeQuestion(category=INTUITIVE,
                      text="I find it easier to learn concepts."),
    HandshakeQuestion(category=INTUITIVE,
                      text="If I were a teacher, I would rather teach a course that deals with ideas and theories."),
    HandshakeQuestion(category=VISUAL,
                      text="I like teachers who put a lot of diagrams on the board."),
    HandshakeQuestion(category=VISUAL,
                      text="I tend to picture places I have been easily and fairly accurately."),
    HandshakeQuestion(category=VISUAL,
                      text="I remember what I see."),
    HandshakeQuestion(category=VISUAL,
                      text="For entertainment, I would rather watch TV."),
    HandshakeQuestion(category=VISUAL,
                      text="When I meet people at a party, I am more likely to remember what they looked like."),
    HandshakeQuestion(category=VERBAL,
                      text="I like teachers who spend a lot of time explaining."),
    HandshakeQuestion(category=VERBAL,
                      text="I tend to picture places I have been with difficulty and without much details.", ),
    HandshakeQuestion(category=VERBAL,
                      text="I remember what I hear.", ),
    HandshakeQuestion(category=VERBAL,
                      text="For entertainment, I would rather read a book.", ),
    HandshakeQuestion(category=VERBAL,
                      text="When I meet people at a party, I am more likely to remember what they said about themselves."),
    HandshakeQuestion(category=SEQUENTIAL,
                      text="When I solve math problems, I usually work my way to the solution one steps at a time.", ),
    HandshakeQuestion(category=SEQUENTIAL,
                      text="When considering a body of information, I am more likely to focus on details and miss the big picture.", ),
    HandshakeQuestion(category=SEQUENTIAL,
                      text="When I am analyzing a novel, I think of individual incidents and try to figure out the themes.", ),
    HandshakeQuestion(category=SEQUENTIAL,
                      text="It is more important to me that an instructor lays out the material in clear sequential steps.", ),
    HandshakeQuestion(category=SEQUENTIAL,
                      text="When solving problems in a group, I would be more likely to think of the steps in the solution process."),
    HandshakeQuestion(category=GLOBAL,
                      text="When I solve math problems, I often just see the solutions but then have to figure out the steps to them."),
    HandshakeQuestion(category=GLOBAL,
                      text="When considering a body of information, I am likely to try to understand the big picture before the details."),
    HandshakeQuestion(category=GLOBAL,
                      text="When I am analyzing a novel, I just know what the general themes are when I finish reading."),
    HandshakeQuestion(category=GLOBAL,
                      text="It is more important to me that an instructor gives me an overall picture and relates to other subjects."),
    HandshakeQuestion(category=GLOBAL,
                      text="When solving problems in a group, I would likely to think of applications of solutions in a range of areas."),
    HandshakeQuestion(category=SELF_PERCEPTION,
                      text="Reasoning skills used to understand math can be helpful to me in my everyday life."),
    HandshakeQuestion(category=SELF_PERCEPTION,
                      text="Learning math changes my ideas about how the world works."),
    HandshakeQuestion(category=SELF_PERCEPTION,
                      text="I'm satisfied if I can do the exercises for a math topic, even if I don't understand how everything works."),
    HandshakeQuestion(category=SELF_PERCEPTION,
                      text="Nearly everyone is capable of understanding math if they work at it."),
    HandshakeQuestion(category=SELF_PERCEPTION,
                      text="There is usually more than one correct approach to solving a math problem."),
    HandshakeQuestion(category=SELF_PERCEPTION,
                      text="Math ability is something about a person that cannot be changed very much."),
    HandshakeQuestion(category=SELF_PERCEPTION,
                      text="Being good at math requires natural (i.e. innate, inborn) intelligence in math."),
    HandshakeQuestion(category=SELF_PERCEPTION,
                      text="I get upset easily when I am stuck on a math problem."),
    HandshakeQuestion(category=SELF_PERCEPTION,
                      text="For each person, there are math concepts that they would never be able to understand, even if they tried."),
    HandshakeQuestion(category=SELF_PERCEPTION,
                      text="If I get stuck on a math problem, there is no chance that I will figure it out on my own.")
])

"""
Question - Category, text

Answer - Question, response

Handshake - many answers
"""
