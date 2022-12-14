import random

from model import Section, Question

sections = [
    Section('天真的人', [
        Question('我会很自然地信任别人'),
        Question('我总能看到生活的光明面，相信生活是积极的'),
        Question('我觉得这个世界整体而言是安全的，人们的意图大都是善良积极的'),
        Question('我对人和世界有信心，相信自己的需要总会得到照顾'),
    ]),
    Section('孤儿/普通人', [
        Question('相比在人群中脱颖而出，我更在意融入群体'),
        Question('结交新朋友时，我往往初始很谨慎，一段时间后才可能建立信任'),
        Question('我是一个现实的人，对生活的期望应该是现实的，才能避免失望'),
        Question('我的共情能力很强，他人的经历很容易唤起我的情感'),
    ]),
    Section('英雄', [
        Question('我喜欢竞争，喜欢在生活的各个方面取胜'),
        Question('我是一个有主见的人，很乐意为我的信仰挺身而出'),
        Question('我能很容易地激励自己，有信心去追求我想要的生活'),
        Question('我是一个坚定的人，当我下决心做某事时，大都会成功执行'),
    ]),
    Section('照料者', [
        Question('我是一个有爱心的人，喜欢帮助别人'),
        Question('我相信对人友善很重要'),
        Question('我是一个慷慨的人，不求回报地助人为乐会让我有获得感'),
        Question('我总是考虑别人先于自己，会自然地关心我周围人的幸福'),
    ]),
    Section('探索者', [
        Question('我就是我，我尽全力活出自己的人生'),
        Question('我习惯性地寻找更好的生活方式或做事方式'),
        Question('我常常不满足于现状，似乎总是想要更多'),
        Question('我相信人总能提升自己，享受探索新的可能性'),
    ]),
    Section('爱人', [
        Question('我喜欢与人交流，并帮助他人建立联系'),
        Question('我对生活充满热情，在追求自己真正喜欢的东西时很有激情'),
        Question('我喜欢与人有深入亲密的，而非肤浅的关系'),
        Question('对我来说，浪漫是很自然的事，当我感受到爱时，生活似乎更有意义'),
    ]),
    Section('规则破坏者/反叛者', [
        Question('此时此刻，我的生活正在经历快速变化'),
        Question('我觉得我的人生观正在发生变化，这可能会导致我做出重大改变'),
        Question('我喜欢颠覆，会放弃生活中不再适用于我的事物与想法'),
        Question('我正在成长为一个独立的个体，并正在重塑自我'),
    ]),
    Section('创造者', [
        Question('我觉得我是一个有创造力的人，很容易受到启发、产生灵感'),
        Question('我的生活就是我的作品，我享受创造它的过程'),
        Question('我很有想象力，能很容易地在脑海中勾勒出我想创造的东西'),
        Question('我常常会有很多活跃的想法，多于我所能采取的行动'),
    ]),
    Section('统治者', [
        Question('我认为自己很有责任感'),
        Question('我会自然地想掌控局势，即使那不是我的角色或任务'),
        Question('我认为自己是一个领导者，并相信自己具有领导能力'),
        Question('我希望我的生活环境是稳定的，想避免混乱'),
    ]),
    Section('魔术师', [
        Question('我喜欢成为变革的催化剂，并将自己视为变革的领导者'),
        Question('我相信我的想法决定了我的生活体验，通过改变我的想法，我可以改变我的生活'),
        Question('我发现自己很容易影响他人，我的存在会对他人产生实在的影响'),
        Question('我对转变很自在，甚至会享受混乱'),
    ]),
    Section('智者', [
        Question('我相信客观性，做事时力求客观'),
        Question('我是一个深思熟虑的人，喜欢分析周围发生的事情'),
        Question('我善于从多种角度看待问题，喜欢挑战以不同的方式思考'),
        Question('我是一个积极的怀疑主义者，“了解真相”对我来说很重要'),
    ]),
    Section('小丑', [
        Question('我喜欢让人发笑，人们认为和我在一起很有趣'),
        Question('我能很自然地看到事物幽默的一面，并“照亮”周围的人'),
        Question('生活是用来享受的，否则一切都毫无意义，“笑对人生”是幸福的真谛'),
        Question('我很自然地活在当下，而非活在未来计划中或沉溺于过去'),
    ]),
]

question_list = []
for section in sections:
    question_list.extend(section.questions)
random.seed()
random.shuffle(question_list)
