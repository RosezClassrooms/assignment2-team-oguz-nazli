from abc import ABC, abstractmethod


class Robot:
    def __init__(self, bipedal="", quadripedal="", wheeled="", flying="", traversal=[], detection_systems=[]):
        self.bipedal = bipedal
        self.quadripedal = quadripedal
        self.wheeled = wheeled
        self.flying = flying
        self.traversal = traversal
        self.detection_systems = detection_systems

    def __str__(self):
        msg = f"{self.bipedal}{self.quadripedal}{self.wheeled}{self.flying} robot. \n"
        if self.traversal:
            msg += "Traversal modules installed:\n"
        for module in self.traversal:
            msg += "-" + str(module) + "\n"
        if self.detection_systems:
            msg += "Detection systems installed:\n"
        for system in self.detection_systems:
            msg += "-" + str(system) + "\n"
        return msg


class BipedalLegs:
  def __str__(self):
    return "TWO LEGS"

class QuadripedalLegs:
  def __str__(self):
    return "FOUR LEGS"

class Arms:
  def __str__(self):
    return "TWO ARMS"

class Wings:
  def __str__(self):
    return "WINGS"

class Blades:
  def __str__(self):
    return "BLADES"

class FourWheels:
  def __str__(self):
    return "FOUR WHEELS"

class TwoWheels:
  def __str__(self):
    return "TWO WHEELS"

class CameraDetectionSystem:
  def __str__(self):
    return "CAMERAS"

class InfraredDetectionSystem:
  def __str__(self):
    return "INFRARED"


class RobotBuilder(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def build_traversal(self):
        pass

    @abstractmethod
    def build_detection_system(self):
        pass


# Concrete Builder class:  there would be MANY of these
class AndroidBuilder(RobotBuilder):
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    # All of the concrete builders have this in common
    # Should it be elevated to the superclass?
    def get_product(self):
        return self.product

    def build_traversal(self):
        self.product.bipedal = BipedalLegs()
        self.product.traversal.clear()
        self.product.detection_systems.clear()
        self.product.traversal.append(BipedalLegs())
        self.product.traversal.append(Arms())

    def build_detection_system(self):
        self.product.detection_systems.append(CameraDetectionSystem())


# Concrete Builder class:  there would be many of these
class AutonomousCarBuilder(RobotBuilder):
    def __init__(self):
        self.product = Robot()

    def reset(self):
        self.product = Robot()

    # All of the concrete builders have this in common
    # Should it be elevated to the superclass?
    def get_product(self):
        return self.product

    def build_traversal(self):
        self.product.wheeled = FourWheels()
        self.product.traversal.clear()
        self.product.detection_systems.clear()
        self.product.traversal.append(FourWheels())

    def build_detection_system(self):
        self.product.detection_systems.append(InfraredDetectionSystem())


class Director:
    @staticmethod
    def make_robot(builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()


director = Director()
builder = AndroidBuilder()
print(director.make_robot(builder))


builder = AutonomousCarBuilder()
print(director.make_robot(builder))


#################### MAIN ##########################
"""bipedal = BipedalLegs()
detection_systems = [InfraredDetectionSystem(), CameraDetectionSystem()]
bot = Robot(bipedal=bipedal, detection_systems=detection_systems)
print(bot)"""
