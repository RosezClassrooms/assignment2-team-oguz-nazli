from abc import ABC, abstractmethod


class Robot:
    # instead of passing None, we just change to empty strings and we append the strings later on.
    def __init__(self, legs="", wheeled="", flying="", numb="", numbup="", traversal=[], detection_systems=[]):
        self.legs = legs
        self.numbUp = numbup
        self.wheeled = wheeled
        self.flying = flying
        self.numb = numb
        self.traversal = traversal
        self.detection_systems = detection_systems

    def __str__(self):  # tried to reduce the number of if statements
        # The reason of 2 if statements actually for displaying purposes.
        msg = f"{self.numb} {self.legs}{self.wheeled}{self.flying} ROBOT. \n"
        if self.traversal:
            msg += "Traversal modules installed:\n"
        for module in self.traversal:
            msg += "-" + self.numbUp + " " + str(module) + "\n"
        if self.detection_systems:
            msg += "Detection systems installed:\n"
        for system in self.detection_systems:
            msg += "-" + str(system) + "\n"
        return msg


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

    def reset(self):
        self.product = Robot()

    def get_product(self):
        return self.product

    @abstractmethod
    def build_traversal(self):
        pass

    @abstractmethod
    def build_detection_system(self):
        pass


# Concrete Builder class:  there would be MANY of these
# UAV and Spider Robot Builder added.
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
        self.product.numb = "SIXTEEEN"
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


class Director:
    @staticmethod
    def make_robot(builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()


if __name__ == '__main__':
    # director using callbacks
    director = Director()
    builder = AndroidBuilder()
    print(director.make_robot(builder))
    builder = AutonomousCarBuilder()
    print(director.make_robot(builder))
    builder = SpiderRobotBuilder()
    print(director.make_robot(builder))
    builder = UAVBuilder()
    print(director.make_robot(builder))

