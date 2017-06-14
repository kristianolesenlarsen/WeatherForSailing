import random
import matplotlib.pyplot as plt
import numpy as np

names = [["What is a type-1 error? What is a type-2 error?", "3","Type 1 errors is the phenomenon of finding significant results when none are in fact present (False positives). Type-2 errors are false negatives, that is failing to identify an effect when there is indeed one present."],
         ["What might pre-analysis plans help with? What are they?", "3","Pre-analysis plans are project descriptions which are prepared before researchers begin their study. They contain information on the hypotheses researchers plan to investigate, and how they will go about it. Their purpose is to restrict the freedom given to researchers in teasing out significant results from their data, thus preventing p-hacking (intentional or not) as well as other kinds of evidence fabrication."],
         ["Describe the differences between conceptual and direct replication", "3","Direct replication reuses the exact procedures of an original rexperiment, and only replaces the datasource with a similar one. Conceptual replication can involve both new data and new procedures, and intends to examine if a result is robust to a variety of changes in environment and procedure."],
         ["How might researchers discover intentional or unintentional mistakes in previous research", "3","By replicating previous studies, which has been underprioritized for a long time. A group of psychologists found that replication studies had hugely reduced mean treatment effects, and that many replication studies didn't even produce significant results."],
         ["Name a previous KU researcher who fabricated results", "3","Milena Penkowa"],
         ["What is plagiarism", "3","The omission of references to previous research either by others or one self, in schientific publications. Plagiarism can have large effects, often costing researchers their jobs"],
         ["Give a definition of moral philosophy in the context of scientific conduct", "3","Moral philosophy is broadly the conceptual study of right and wrong, in terms of scienctific conduct it is the study of how researchers conduct themself in a world of conflicts of interests, incentives to publish in the 'right' journal etc."],
         ["What are nonstandard beliefs?", "3","A concept from behavioral economics, used to describe situations where individuals doesn't have unbiased beliefs, but might instead suffer from problems with bayes updating or probabilities in general. This includes projection bias, which describes situations where people misjudge their reaction to big future changes."],
         ["Define projection bias", "3","Projection bias is a phenomenon where individuals fail to give unbiased estimates of their reactions to future changes, for example misjudging which of two choices their future self would like to make."],
         ["Define non-standard decision making", "3","Situations where individuals horizon is limited or their choices are affected by (seemingly unrelated) context."],
         ["What is the common trait of models in Behavioral Economics, explain the consequences of this trait", "3","They generally include additional parameters to account for the increased conplexity. This in turn gives models more explanatory power, but of course for each paramter included the complexity of the models increase, and in the extreme case we could always include more parameters until we had a perfect fit. Thus we need to devise of a good way to limit our inclusion of additional parameters in the models."],
         ["Give a suggestion to how we could measure the value of adding aditional parameters to a model, to account for behavioral effects", "3","One option would be to rate models on -their ability to account for a range of systematic deviations from standard models- possibly restricted to be independent of context. "],
         ["BE models rarely bring new answers, what do they bring instead?", "3","puzzles"],
         ["Define paternalism, and answer why this is relevant to behavioral economists", "3","Paternalism is the belief that people can and/or should be governed by an authority to their own benefit. The question of parternalism has become relevant in the context of BE as research indicates that individuals are not always rational and/or behaving optimally. This poses the question of whether policy makers should govern people to make rational choices, which is contrary to the economic belief that individuals are free and acts in the best way possible themselves. A proposed answer to this quetion is libertarian paternalism."],
         ["Define libertarian paternalism", "3","libertarian paternalism is the idea that policies should nudge people to make decisions to the benefit of themselves and/or society, while at the same time not restricting individuals abilities to choose suboptimally - that is policies should leave the option-space of individuals unchanged, but can alter the default option."],
         ["What does Thaler and Sunstein call policies which nudge people to act in a certain way, e.g. opt-out organ donor systems?", "3","Libertarian paternalism"],
         ["Is libertarian paternalism efficiency enhancing?","3","It depends. If nudging requires the implementation of secondary regulation (i.e. if we want to nudge people into getting health insurance, we also have to specify what is acceptable as a health insurance policy, and so on) it might actually decrease efficiency."],
         ["Name some benefits of libertarian paternalism","3","1) systematic deviations from efficiency are costly to society, 2) it is less invasive than alternative policies, 3) In many cases it is necessary to specify a default anyways, so we might as well make the default the optimal one and 4) people make choices with or without nudging"],
         ["Name some issues with libertarian paternalism","3","1) the interests of individuals and lawmakers are not necessarily aligned, 2) Nudging encourages passivenes, 3) If people become used to nudging it might loose it's effectiveness, 4) It might be necesarry to create a whole list of -nudging policies- which in turn can decrease efficiency"],
         ["What else than nudging can be considered libertarian paternalism?","3","Framing, labels, reminders, cool-off periods and self commitment devices"],
         ["Behavioral economics is the intersection of which sciences?","3","Economics and psychology"],
         ["Smith, Croson and Gächter propose seven reasons to conduct experiments in economics, for example to test theories and to measure preferences - give some other reasons to conduct experiments.","3","Experiments can explore why theories fail, serve as 'wind tunnels' for policy evaluations, compare institutions and environments, and be used in teaching"],
         ["Can we implement experimental results in the real world and expect the effects to be identical to those found in the lab","3","This is is matter of external validity. Experiments are often run in very controlled settings, and might therefore loose external validity to gain high internal validity. If this is the case we cannot ensure that policies will also work in real life. Some researchers carry out large scale randomization experiments in real institutions, to try and gain external validity. Thus if experimental results hold will always be an open question, which depends on context."],
         ["What are artefactual lab experiments?","3","lab experiments which employ non-standard subject pools, for example doctors in an experiment on disease treatment or game theorists playing prisoners dilemma"],
         ["What are framed field experiments?","3","Experiments which incorporate context, for example fishermen playing the public goods game"],
         ["What are natural experiments?","3","Experiments that take place coincidentally, for example as a result of changes in policy."],
         ["Define internal- and external validity","3","Internal validity is a way to describe the 'likelyhood' that results of an experiment are actually true, within the setting of the experiment. External validity is a way to measure/describe how well the conclusions of an experiment hold up outside of the experiment. "],
         ["Give some reasons why experiments might lack external validity","3","Scrutiny - participants know they're being watched, stakes - stakes in experiments are different from the stakes in real life and experimental restrictions on time horizons and choice sets. (can you name more?) "],
         ["A major concern about the validity of experiments is that they overestimate peoples preferences for fairness - why is this?","3","Because the setting of experiments is inherently unrealistic, it can be said that participants favor fairness more, possibly because they're more concious about the consequences of their choices than they would be in real life."],
         ["Can experiments be deductive?","3","No they're inductive in nature"],
         ["Why is the debate of external validity of lab experiments so prominent in the field of development economics?","3","Because participants tend to be WEIRD (western, educated, industrialzed, rich, democratic) - this makes the external validity of experiments questionable when their results are applied to 3. world contries"],
         ["Provide a definition of science","part 1", "Science is the systematic endeavour to develop and organize knowledge of the world in the form of testable/predictable explanations"],
         ["Describe the key differences between realists and antirealists","part 1", "Realists believe that science converges towards truth. Antirealists maintain that while theories may be useful, they do not in fact represent the true nature of things. A third viewpoint is empiricism, that sees empirical evidence as truth in itself"],
         ["What constitutes a phenomenon?","part 1", "An empirical regularity, that can be inferred through the trace they leave in measurements we can make. Typically measureable but not directly observable. They are to some extent idealized, and should be of scientific interest."],
         ["What is the demarcation rule of the logical positivists?","Part 1", "Logical positivists accept only analytical (true by definition) and synthetic a posteriori (not true by definition, true by experience) statements as scientific"],
         ["What is an analytical statement","Part 1","Analytical statements are true by definition, e.g. 1+1=2"],
         ["How is verification done in logical positivism?","Part 1","Through induction"],
         ["What is the main critique of inductive verification, and what is the response to this criticism?","Part 1", "That induction does not necessarily generalize, e.g. black swans. Response: Probability of truth increases in observations. Counterargument: Not true if observations drawn from same subset of population."],
         ["What is Poppers demarcation line between science and non-science?","Part 1", "Falsification"],
         ["What is Poppers position regarding realism vs. antirealism?","Part 1", "Seems to be antirealist - asserts that theories can never be proven. Long-standing theories are simply deserving of more thorough research"],
         ["What is the role of the 'leap of imagination' to Karl Popper?","Part 1", "The way a new theory replaces an older falsified theory"],
         ["What is an immunizing strategem?","Part 1","A strategy in which theories can incorporate any new information into the theory, such that they are less falsifiable (if at all). Standard example: Freud and denial"],
         ["What is denial in Freud's theories an example of in relation to Popper's view on science?","Part 1","An immunizing strategem"],
         ["What does the Duhem-Quine Thesis relate to, and what does it say?","part 1","Relates to Poppers falsification demarcation line. Is essentially a critique asserting that to test a theory we require background assumptions, and that 'falsification' can be blamed on measurement issues"],
         ["What distinguishes Thomas Kuhns theory of science from the others considered in this course?","Part 1", "Kuhns theory is a positive, not normative, description of science."],
         ["What is the incommensurability thesis?","Part 1", "Relates to Thomas Kuhn, and states that it is meaningless to compare theories from different paradigms"],
         ["How does science progress in the view of Thomas Kuhn?","Part 1","In a normal period, research builds on previous results and ideas, and is based around a paradigm, i.e. a certain thoughtset or viewpoint. When the paradigms proves unable to describe anomalies, a new paradigm materializes as a result of a scientific revolution"],
         ["What is Imre Lakatos known for?","Part 1", "Sophisticated Falsification and his concept of research programmes"],
         ["What is sophisticated falsification?","Part 1","A theory T1 should be abandoned when (and not until) a new theory T2 (i) has excess empirical content, i.e. makes new predictions (ii) contains all unrefuted content of T1, (iii) some of the excess content of T2 is confirmed by experiment or observation"],
         ["What are the elements of a Research Programme (Imre Lakatos)?","Part 1"," A core of theoretical assumptions that cannot be altered or abandoned without abandoning the RP altogether, and a set of more modest theories that seek to explain evidence that threaten the core."],
         ["How would Popper view Lakatos' idea of Research Programmes?","Part 1","Would be skeptical, RP idea resemble Immunizing Strategems!"],
         ["What determines whether a Research Programme is considered degenerative or progressive?","Part 1","Whether recent developments has decreased or increased the predictive power of the theory"],
         ["How should theories be evaluated according to Friedmann?","part 1","By their ability to predict. Longer: By their predictive power relative to their simplicity."],
         ["What are the criticisms of Friedmanns views?","Part 1","Prediction is not the only purpose of economics, control and explanation is also important"],
         ["What is Samuelsons position?","Part 1","Strict unrealism is a scientific sin (as a response to Friedman), instead Samuelson assumes a position of descriptivism, where a valid system is equal to its complete set of empirical consequences, all of which should be tested."],
         ["What is an explanandum?","part 1","The thing to be explained in the D-N model"],
         ["What is the deductive-nomological model?","part 1", "A model of explanation. Consists of a set of true statements of initial conditions, scientific laws and deduces from them the explanandum"],
         ["Describe the critique of the D-N model","part 1","Symmetry and that the the explanandum may follow from the initial statements and scientific laws, but that it does not necessarily describe the causality accurately (e.g. George doesn't get pregnant)"],
         ["What is David Humes definition of causality?","part 1", "(i) X is universally associated with Y, (ii) Y follows X in time, (iii) X and Y are spatio-temporally contiguous (no gaps in time/space between X and Y)"],
         ["What are the two definitions of economics given by Rodrik?","Part 1","A) Subject-matter: The social science devoted to understanding how the economy work, B) Method: A way of doing social science using tools such as mathematics and statistics"],
         ["What are the two analogies Rodrik offers for models in economics?","part 2","(i) Models as fables (sacrifice realism for clarity and offer a transparent moral (ii) Models as experiements (model is equivalent to a lab-setup)"],
         ["Describe the issues of internal and external validity","part 2","Internal validity: How clear the effect of the mechanism investigated is within the experiment, external validity: How well the conclusion 'travels' to other settings"],
         ["What is the definition of a critical assumption in the sense that Rodrik uses it?","part 2","An assumption that if altered in a more realistic direction produces significantly different outcomes."],
         ["What are the advantages and disadvantage(s) of using math in economics?","part 2","Advantages: Clarity and consistency. Disadvantages: Comprehensibility barrier"],
         ["What does the second-best option theorem state?","part 2","If one optimum condition cannot be satisfied, other optimum conditions will generally change as well"],
         ["What are the barrels (horizontal or vertical boards) an analogy for?","Part 2","The presence of a binding constraint"],
         ["What are the principals of model selection?","Part 2","(i) Verifying critical assumptions. (ii) Verifying that the postulated mechanisms are actually operating (iii) verifying the direct implications of the model (iv) Verifying incidental consequences of the model"],
         ["What kinds of inference do we use when building models and formulating theories?","Part 2","Forward inference when building models, reverse causal inference when constructing theories"],
         ["Describe manufactured preferences","Part 2","Preferences that are endogenous or 'manufactured' through advertisement, social media etc. This raises questions as to the arguments for free markets."],
         ["Describe the issues regarding the moral limits of markets","Part 2","Some things may hold infinite intrinsic value (e.g. your kids), or market mechanism rejected out of moral or ethical reasons. (e.g. unwillingness to commodify organs)"],
         ["What is Ariel Rubinsteins critique regarding Rodriks argument that economics is a science?","Part 2","Rubenstein argues that the reasons that economics is a science could equally well apply to history or literature"],
         ["What are Deaton and Cartwright's thoughts on the issue of traveling from research to policy?","Part 2","Travelling from experiment to policy needs to be done with the same rigor and caution and the research itself"],
         ["What are the three types of reasoning outlined by Eichengreen?","part 2","Inductive reasoning, deductive reasoning and analogical reasoning"],
         ["What is Schiller & Schillers views on modern economists?","part 2","They are critical of the tendency for ever narrower specialization"]]


def runner(x):
    l = []
    i = 0
    for i in range(1,len(x)+1):
        prog = list(map(int, x[0:i]))
        meanSoFar = sum(prog)/ i
        l.append(meanSoFar)
    return l


def counter(x, Q):
    x = list(map(int,x))
    c = []
    for i in range(0,len(Q)):
        N = x.count(i)
        c.append(N)
    return c


def tester(Q):
        n = int(round(random.uniform(0,len(Q)),0))
        x = Q[n][0]
        number.append(n)
#        print(x)
        a = input( x + " - hit 'Enter' when ready for answer, 'stop' to terminate")

        if a != "stop":
            if input(Q[n][2] + " - hit 'Enter' to try another one; 'stop' to terminate. -------------------------------------------------------------------------------------------------------------------" + "YOUR ANSWER was:" +  a) != "stop":
                res = input("Did you get it right (0/1)")
                if res == "1" or res == "0":
                    results.append(int(res))
                else:
                    results.append(0)
                tester(Q)

def sort(Q,part):
    out = []
    for i in range(0,len(Q)):
        if Q[i][1].lower() == part.lower():
            out.append(Q[i])
    return out


part1 = sort(names, "part 1")
part2 = sort(names,"Part 2")
part3 = sort(names,"3")



results = []
number = []

tester(part2)


avg = runner(results)

plt.plot(results, label = "result of guess")
plt.plot(avg, label = "average correct rate")
plt.legend()
plt.suptitle("Quiz score")
plt.show()





count = counter(number, names)

plt.bar(list(range(0,len(names))), count, align = 'center', alpha = 0.5)
plt.suptitle("Number of occurences of each question")
plt.show()
