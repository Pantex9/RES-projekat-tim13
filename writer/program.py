from writer import Writer
from replicator_sender import ReplicatorSender


def main():
    repl_sender = ReplicatorSender()
    writer = Writer(repl_sender)
    writer.writer_send_data()
    writer.writer_send_data()
    writer.writer_send_data()


if __name__ == "__main__":
    main()
