from dataclasses import dataclass

from src.shared.domain.bus.command.command import Command


@dataclass
class CreateCourseCommand(Command):
    id: str
    title: str
