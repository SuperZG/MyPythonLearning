import unittest
from survey import AnonymousSurvey


# 验证存储store_responses方法是否有效
class TestAnony(unittest.TestCase):
    ''' test AnonmyousSurvey class'''

    # 对类进行测试的时候，我们可能要测试多种情况，需要定义多种方法，每种方法的代码块中生成一个类的实例。
    # 比如上例，我们测试了三个样本的存储的方法，类的实例为test_survey, 如果我们再定义一个存储单个样本的方法，还需要生成一个类实例。代码存在重复。
    # 我们可以使用setup()方法，在unittest.Testcase中，如果我们包含了setup()方法，会首先运行该setup(), 然后再执行其余的以test开头的其他方法。
    # 我们对类的测试代码进行修改，新增一个setUp()方法，用于初始化目标类的实例，我们提供了一个question作为实例初始化时的参数。
    # 在另外两个以test打头的测试方法中，我们直接调用初始化后的实例，而不用重新生成实例，优化了代码的结构。运行结果与之前相同
    def setUp(self):
        question = 'What kind of language are you using?'
        self.test_survey = AnonymousSurvey(question)
        self.responses = ['Java', 'PHP', 'Rust']

    def test_single_response(self):
        question = 'What kind of language are you using?'
        test_survey = AnonymousSurvey(question)
        test_survey.store_responses('Python')
        # assertIn 判断元素是否在list中
        self.assertIn('Python', test_survey.responses)

    def test_multi_response(self):
        question = 'What kind of language are you using?'
        test_survey = AnonymousSurvey(question)
        responses = ['Rust', 'Javascript', 'PHP']
        for response in responses:
            test_survey.store_responses(response)
        for response in responses:
            self.assertIn(response, test_survey.responses)


if __name__ == '__main__':
    unittest.main()
