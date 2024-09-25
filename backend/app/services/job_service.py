import tensorflow as tf
import tensorflow_hub as hub


class JobService:
    def __init__(self) -> None:
        self.bert_model = hub.load(
            "https://tfhub.dev/google/universal-sentence-encoder/4"
        )

        # A sample in-memory storage; replace this with database code.
        self.db = []

    def create_job(self, job) -> None:
        pass

    def get_jobs(self, cursor: int = None) -> None:
        pass

    def get_job_by_id(self, job) -> None:
        pass

    def match_jobs_to_resume(self, resume_text: str) -> None:
        # Todo: use vector DB
        job_texts = [job.description for job in self.db]
        resume_embedding = self.bert_model([resume_text])
        job_embeddings = self.bert_model(job_texts)
        similarities = tf.matmul(resume_embedding, job_embeddings, transpose_b=True)
        similarity_scores = similarities.numpy()[0]
        matched_jobs = sorted(
            self.db, key=lambda job: similarity_scores[job.id - 1], reverse=True
        )
        return matched_jobs
