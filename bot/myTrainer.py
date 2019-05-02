from chatterbot.trainers import Trainer
from chatterbot.conversation import Statement
from chatterbot import utils


class DummyTrainer(Trainer):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def train(self, qaset):

        statements_to_create = []

        for qa_count, qa in enumerate(qaset):
            if self.show_training_progress:
                utils.print_progress_bar(
                    'Dummy QA Trainer',
                    qa_count + 1, len(qa)
                )

            question = qa[0]
            answers = qa[1:]
            for answer in answers:
                statement = self.get_preprocessed_statement(
                    Statement(
                        text=answer,
                        in_response_to=question,
                        conversation='training'
                    )
                )
                statements_to_create.append(statement)
        self.chatbot.storage.create_many(statements_to_create)
