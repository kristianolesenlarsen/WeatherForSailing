import random
import matplotlib.pyplot as plt
import numpy as np

names = [["Checchi","Credit constraints","say that if there are credit constraints we should expect more unequal countries (countries with high gini) to have lower enrollment rates. Similarly we should expect a positive relationship between public spending as  a share of GDP and enrollment. He tests this using cross country data on enrollment rates in primary, secondary and higher education. He only find significant results for secondary education, and stronger effects for girls across all  groups. There is large explanatory power in the 1-below level of education (i.e. primary educ completion rates explain secondary education enrollment) suggesting a 'ratchet effect'. His results are criticized for being near-insignificant and his approach of using the gini."],
        ["Who claims that the gini coefficient and educational enrollment figures can be used to show the presence of credit constraints?","checchi","Checchi, because if credit constraints are present more inequality should lead to lower enrollment rates, which there is evidence for only in secondary schools. "],
        ["Belley, Lochner","Credit constraints","Compares two cohorts in the NLSY (National longitudinal survey of youth) to investigate the effects of family income on education. As measures of ability they use army test scores. They find that ability is more important in the bottom of the family income distribution, and that income has become more important from 79 to 97. While ability has become more important at the bottom, it has become less important at the top. "],
        ["Keane, Wolpin","Credit constraints","find that students are tightly constrained in their credit options, but that these constraints doesn't matter much for completion rates, as reducing them would only increase labor supply while studying."],
        ["Who claims reducing credit constraints would only increase labor supply of students?","KW","Keane, Wolpin"],
        ["Carneiro, Heckman","Credit constraints","find small gaps in college attainment by family income after controlling for ability. They say this is the case because ones financial situation at age 17 is the result of long run factors, so the constraints are binding far before it's time to send college applications. "],
        ["Who claims that credit constraints are not important for college attendance, why?","CH","Carneiro, Heckman - because by controling for ability at age 17 they can remove the significance of credit constraints, they interpret this as showing that credit constraints at college age are a result of long run factors, that have been binding long before age 17"],
        ["Duflo","Returns","studies the indosnesian INPRES program of school construction. He finds a very large return to a year of education by comparing children who attended before and after the new schools were constructed."],
        ["The Perry Preschool project","Skill formation","studies low ability children from disadvantaged homes. They randomly assign children to a treatment of two years of extra teaching, while their parents are also coached in socioeconomic factors. They find short term increases in cognitive abilities, but on factors like lifetime income and incarceration participants do much better than the control group. This suggests non-cognitive abilities are of great importance, which also shows from a comparison of parents valuation of 'good parenting' before and after the treatment - parents become significantly more aware of the importance of parenting."],
        ["Cunha, Heckman","Skill formation","build a many-period model with several periods of childhood to as best as possible match 'stylized facts' in economics of education. They include sensitive and critical periods of childhood, and derive both static and dynamic complementarity of investments and innate ability. "],
        ["Hoxby","Production of HC","use natural variation in enrollment due to fluctuations of births as well as changes in minimum schooling laws. He finds no significant effect of class size in grades 4,6 and 8."],
        ["Who uses variation in birth cohort sizes to show no significant effects from class sizes on test scores?","H","Hoxby"],
        ["Angrist, Lavy","Production of HC","Use an old Israeli rule that school classes must be divided in half when they exceed 40 students. They find significantly higher test scores in smaller classes in 4th and 5th grade. Their work suffers form problems with endogeneity of parents resudential choices, and because they only have variation between classes of size 20 and 40 (no lower)."],
        ["Calmar et al.","Production of HC","randomly assigns schools with money to hire extra co-teachers. Schools can either hire a co-teacher with or without a degree. There's generally no effect on math grades, only on reading grades. They find that co-teachers w.o. degrees are most helpful and helps children with low education parents the most. teachers with degrees help those with more able parents, and possibly the most disadvantaged in math."],
        ["Krueger","Production of HC","randomly assigns children to different class sizes and find small increases in performance. There is however evidence that enrollment rates to college increase for those in smaller classes. They had problems with parents withdrawing from the program if their children ended in large classes"],
        ["Who estimates the effect of class sizes by randomly assigning children to different sized classes, what does he find and problems does he have","K","Krueger, he finds small effects from class size on academic performance, but signs that children from small classes are more likely to attend higher education. He faced problems with parents withdrawing their children from the program if they were assigned to a large class"],
        ["Woesmann, West","Production of HC","look at the TIMSS data (Third International Maths and Science Study) across countries. Instead of using natural experiments they use school fixed effects to compare class sizes. They find that smaller classes are only beneficial for math grades in France and Iceland, while they matter for Science in Greece and Spain. In the remaining countries they find no effects. They further document that the four countries have lower than average performance, and educational expenditures. Greece and Iceland further pays teachers a below average salary. This could be evidence that class size only matters when teachers are not skilled to handle large classes."],
        ["Mazumder","Intergenerational persistence","engages in a discussion of the size of rho. Others have previously suggested that it's in the range of 0.2 to 0.35, but Mazumder claims these all have large issues because estimates of lifetime income are impossible to get precise. Using statistical techniques he estimates rho to be arrond 0.6. "],
        ["Björklund et al.","Intergenerational persistence","use Swedish adoptees to decompose genetics from environment in the intergenerational persistence equation. They find about equal contributions from biological parents and foster parents. Their study have been criticized as they assume that the transfer from bio- to foster parents happens at birth and assumes randomness in who gets which children. "],
        ["Twin studies","Intergenerational persistence","use twins to identify the causal returns to education, amongst other things. They are generally good studies but are critiqued for assuming that twins are identical - if they were they should also act the same - in other words, there's no guarantee that they don't vary on unobservables just because they're twins."],
        ["Lochner, Moretti","Crime","use IV estimates on state specific changes in compulsory schooling laws to investigate the effect of education on crime. Their findings suggest large returns to education as it prevents crime. They use self-reported crime from the NLSY to avoid measurement errors, but have large problems with underreporting (for example on rape)."],
        ["Who uses self reported crime statistics to show large effects from education on crime reduction?","LM","Lochner, Moretti"],
        ["Lleras, Muney","Health","use three census cohorts, each separated by one decade to calculate death rates between them. They face some problems with imprecise death rate calculations, giving them negative death rates for some ages, but continue nonetheless. They then use state specific changes in compulsory schooling laws from 1915-1939 as a quasi-experiment, to investigate of schooling matters for lifetime through a regression discontinuity setup. They find significant results for the 10-year death rate on a number of regressions. Using IV they get higher estimates, suggesting a concave relationship between education and health. Years of compulsory schooling also provides significant results. "],
        ["Grossman","Health","Builds a dynamic model where health is an investment good, and affects the time of life, thereby altering the expected return to education."],
        ["Who gains from specific OTJ training","training","Specific OTJ training doesn't affect the outside options of workers, so firms can still pay them a low wage compared to their marginal product. Since abilities are specific the desicion to train workers will depend on the turnover rate, and workers can get small wage increases to retain them."],
        ["How will wages of workers who recieve general OTJ training develop?","training","Specific OTJ training alters the opportunity costs of workers, so firms have to pay them their marginal product. But for firms to be incentivized to provide training, workers must suppress their wages when young, and reap the benefits later in life, leading to a convex wage curve"],
        ["Describe the requirements for a separating signaling equilibrium","signalling","The high-skill wage set by the firm must be high enough for high-skill workers to prefer it and low enough that low-skill workers still prefer not going to school."],
        ["Is signaling efficient?","signalling","No, since education is not productive it is a unnessecary cost"],
        ["Rand experiment","Health","randomly assigned US individuals to one of five specifically designed health insurance plans. They found little effect from health insurance on health, except for small subgroups of their population. The general conclusion was that increasing health insurance would be less cost effective than effective educational interventions. "],
        ["What is the main takeaway from the large experiment in Health Insurrances?, what was it called?","R","That the health returns to increasing insurance coverage are lower than the health returns from education - it was called the Rand Health Insurance Experiment"],
        ["Barro","Growth","finds results indicating that extra schooling does increase the GDP growth rate."],
        ["Behrman, Birdsall","Growth","Criticizes previous research into the relationship between growth and education for not taking into account the differences in the quality of education. They say quality is at least as important as quantity."],
        ["Hanushek (Kimko, Wössmann)","Growth","use international test data as proxy for the quality of education, they find significant and large results of quality of education on growth compared to the effect of quantity of education. Their approach makes years of schooling insignificant."],
        ["Who uses international test result data as  a proxy for the quality of education, what do they find?","HKW","Hanushek (with Kimko and Wössman) - they find that quality is far more important than quantity of education"],
        ["Why is the Mincer equation often estimated in economics?","M","Because it provides a useful benchmark for studies of the returns to education although it's doubtful that estimates are causal. With a set of strict assumption the main parameter can be interpreted as the internal rate of return to education"],
        ["Dobbie, Fryer","production","Use oversubscribed NYC charter schools to estimate factors of production for HC - they find little evidence that 'traditional' measures are effective, but suggests that frequent teacher feedback, high dosage tutoring and high instruction time all are effetive at explaining school effectiveness"],
        ["Autor, Dorn","Polarization","observe a large increase in wage inequality. Unlike what the ordinary SBTC hypothesis would say, the changes are not monotone, as both employment and wages at the lowest paying jobs have also increased. They say service jobs account for the large increase in low-wage jobs. They construct a model to explain the phenomena, and finds that employment polarization happens when the elasticity of substitution between computers and routine labor (in production) is larger than the elasticity of substitution between goods and services (in consumption)."],
        ["What happens to the gender wage gap in the use-skill bias SBTC hypothesis?","SBTC","it decreases for low income groups but increases for high income groups because of the use gradients, i.e. that more low wage females use pc's than low wage males, while at the top of the income distribution it's opposite"],
        ["What happens to the gender wage gap in the rising skill-price SBTC hypothesis?","SBTC","It should increase, as men earn higher wages, often atributed to unobserved ability. If this is the case the increasing returns to skill should increase male wages"],
        ["When did wage inequality increase the most?","SBTC","In the 1980's, which is a puzzle for the SBTC hypothesis since computer evolution continued into the 90's and 2000's"],
        ["Why are pencils a puzzle to the SBTC","SBTC","because on german data they show a return in the same type of regressions as previously used to show there is a return to using a computer on the job."],
        ["What does becker define as the egalitarian case","Woytinski","A situation where everybody are identical in terms of abilities, and thus their recieved education is only dependent on the supply of education they face."],
        ["In the median voter model - will there be over- or underproduction of HC if we are in the elite case?","median voter","It depends on the distribution of abilities, bu assuming they are right-skewed there will be underproduction of human capital when everybody have the same wealth"],
        ["Where in the income distribution does abilities matter the most, and according to who?","Credit constraints","At the bottom of the income distribution. Income has become more important from 79 to 97 in all parts of the distribution (Belley, Lochner)"],
        ["Who uses changes in compulsory schooling laws to show reduced deathrates when educational attainment increases","LM","Lleras, Muney - they find higher estimates with IV compared to OLS, suggesting a concave relationship between education and health"],
        ["What is Maimonides rule? What have it been used to study?","M","An old Israeli rule stating that when classes exceede 40 students they should be divided in two equally sized classes. It has been used to study the effect of class size on education"],
        ["Who use TIMSS data, what for and what do they find?","WW","Woesmann and West - they study the effect of smaller class sizes and find that effects are limited to few countries. In those countries where effects are present, it's likely that the reason is a mix of different effects including low teacher wages"]]



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


results = []
number = []

def tester():
        n = int(round(random.uniform(0,len(names)),0))
        x = names[n][0]
        number.append(n)
#        print(x)

        if input( x + " - hit 'Enter' when ready for answer, 'stop' to terminate") != "stop":
#            print(names[n][2])
            if input(names[n][2] + " - hit 'Enter' to try another one; 'stop' to terminate") != "stop":
                res = int(input("Did you get it right (0/1)"))
                results.append(res)
                tester()


tester()

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
