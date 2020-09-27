from abc import ABC, abstractmethod


class Robot:
    # instead of passing None, we just change to empty strings and we append the strings later on.
    # What is done?
    # Component types are added so we're not specify components like two legs, just using like legs
    # few parameters added, rotors => another component
    # numb => number of components (if legs and numb = 2 then robot has two legs)
    # numbUp => number of components of upper body of the robot (number of arms or blades)
    def __init__(self, legs="", wheeled="", flying="", rotors="", numb="", numbup="", traversal=[], detection_systems=[]):
        self.legs = legs
        self.numbUp = numbup
        self.wheeled = wheeled
        self.flying = flying
        self.rotors = rotors
        self.numb = numb
        self.traversal = traversal
        self.detection_systems = detection_systems

    def __str__(self):  # tried to reduce the number of if statements
        # The reason of 2 if statements actually for displaying purposes or debugging.
        msg = f"{self.numb} {self.rotors}{self.legs}{self.wheeled}{self.flying} ROBOT. \n"
        if self.traversal:
            msg += "Traversal modules installed:\n"
        for module in self.traversal:
            msg += "-" + self.numbUp + " " + str(module) + "\n"
        if self.detection_systems:
            msg += "Detection systems installed:\n"
        for system in self.detection_systems:
            msg += "-" + str(system) + "\n"
        return msg


# Concrete classes doesn't specify numbers anymore
class Rotors:
    def __str__(self):
        return "ROTORS"


class Legs:
    def __str__(self):
        return "LEGS"


class Arms:
    def __str__(self):
        return "ARMS"


class Wings:
    def __str__(self):
        return "WINGS"


class Blades:
    def __str__(self):
        return "BLADES"


class Wheels:
    def __str__(self):
        return "WHEELS"


class CameraDetectionSystem:
    def __str__(self):
        return "CAMERAS"


class InfraredDetectionSystem:
    def __str__(self):
        return "INFRARED"


class RobotBuilder(ABC):
    # Common methods implemented in super class here.
    def __init__(self):
        self.product = Robot()

    # Common methods implemented in super class here.
    def reset(self):
        self.product = Robot()

    # Common methods implemented in super class here.
    def get_product(self):
        return self.product

    # abstract methods passed just like the abstract factory pattern.
    @abstractmethod
    def build_traversal(self):
        pass

    # abstract methods passed just like the abstract factory pattern.
    @abstractmethod
    def build_detection_system(self):
        pass


# Concrete Builder class:  there would be MANY of these
# UAV, Spider Robot and QuadCopter Builder added.
class AndroidBuilder(RobotBuilder):
    def build_traversal(self):
        self.product.legs = Legs()
        self.product.numb = "TWO"
        self.product.numbUp = "TWO"
        self.product.traversal.append(Legs())
        self.product.traversal.append(Arms())

    def build_detection_system(self):
        self.product.detection_systems.append(CameraDetectionSystem())


class AutonomousCarBuilder(RobotBuilder):
    def build_traversal(self):
        self.product.wheeled = Wheels()
        self.product.numb = "FOUR"
        self.product.traversal.clear()
        self.product.detection_systems.clear()
        self.product.traversal.append(Wheels())

    def build_detection_system(self):
        self.product.detection_systems.append(InfraredDetectionSystem())
        self.product.detection_systems.append(CameraDetectionSystem())


class SpiderRobotBuilder(RobotBuilder):
    def build_traversal(self):
        self.product.legs = Legs()
        self.product.numb = 16  # User can insert integer instead of string as well.
        self.product.traversal.clear()
        self.product.detection_systems.clear()
        self.product.traversal.append(Legs())

    def build_detection_system(self):
        self.product.detection_systems.append(InfraredDetectionSystem())


class UAVBuilder(RobotBuilder):
    def build_traversal(self):
        self.product.flying = Wings()
        self.product.numb = "TWO"
        self.product.traversal.clear()
        self.product.detection_systems.clear()
        self.product.traversal.append(Wings())

    def build_detection_system(self):
        self.product.detection_systems.append(InfraredDetectionSystem())
        self.product.detection_systems.append(CameraDetectionSystem())


class QuadCopterBuilder(RobotBuilder):
    def build_traversal(self):
        self.product.rotors = Rotors()
        self.product.numb = 4  # User can insert integer instead of string as well.
        self.product.traversal.clear()
        self.product.detection_systems.clear()
        self.product.traversal.append(Rotors())

    def build_detection_system(self):
        self.product.detection_systems.append(CameraDetectionSystem())


class Director:
    @staticmethod
    def make_robot(builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()


def debugging():
    detection_systems = [InfraredDetectionSystem(), CameraDetectionSystem()]
    bot = Robot(legs=Legs(), numb=2, detection_systems=detection_systems)
    print(bot)


def main():
    director = Director()
    builder = AndroidBuilder()
    print(director.make_robot(builder))
    builder = AutonomousCarBuilder()
    print(director.make_robot(builder))
    builder = SpiderRobotBuilder()
    print(director.make_robot(builder))
    builder = UAVBuilder()
    print(director.make_robot(builder))
    builder = QuadCopterBuilder()
    print(director.make_robot(builder))


if __name__ == '__main__':
    main()
    # debugging()