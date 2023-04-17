import math
from p5 import (
    circle,
    background,
    text,
    run,
    textWidth,
    size,
    no_stroke,
    stroke,
    LEFT,
    RIGHT,
)
import random
import array
from IVector import IVector


class Boid:
    def __init__(self, x, y, width, height, color=255):
        self.color = color
        self.width = width
        self.height = height
        self.max_speed = 10
        self.perception = 100
        self.max_force = 1
        self.position = IVector([x, y])
        vec = array.array(
            "f", [(random.random() - 0.5) * 10, (random.random() - 0.5) * 10]
        )
        self.velocity = IVector(vec)
        vec = array.array(
            "f", [(random.random() - 0.5) / 2, (random.random() - 0.5) / 2]
        )
        self.acceleration = IVector(vec)

    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration  # limit
        if self.velocity.norm() > self.max_speed:
            self.velocity = self.velocity / self.velocity.norm() * self.max_speed
        self.acceleration = IVector(array.array("f", [0, 0]))

    def show(self):
        stroke(self.color)
        circle(self.position.get_value(0), self.position.get_value(1), 10)

    def edges(self):
        if self.position.get_value(0) > self.width:
            self.position.set_value(0, 0)
        elif self.position.get_value(0) < 0:
            self.position.set_value(0, self.width)
        if self.position.get_value(1) > self.height:
            self.position.set_value(1, 0)
        elif self.position.get_value(1) < 0:
            self.position.set_value(1, self.height)

    # Proprietatea de a se orienta in directia miscarii flotei
    def align(self, boids):
        steering = IVector(array.array("f", [0, 0]))
        total = 0
        avg_vec = IVector(array.array("f", [0, 0]))
        for boid in boids:
            if (boid.position - self.position).norm() < self.perception:
                avg_vec += boid.velocity
                total += 1
        if total > 0:
            avg_vec /= total
            avg_vec = IVector(avg_vec.get_values())
            avg_vec = (avg_vec / avg_vec.norm()) * self.max_speed
            steering = avg_vec - self.velocity
        return steering

    # Proprietatea de a se apropia de flota
    def cohesion(self, boids):
        steering = IVector(array.array("f", [0, 0]))
        total = 0
        center_of_mass = IVector(array.array("f", [0, 0]))
        for boid in boids:
            if (boid.position - self.position).norm() < self.perception:
                center_of_mass += boid.position
                total += 1
        if total > 0:
            center_of_mass /= total
            center_of_mass = IVector(center_of_mass.get_values())
            vec_to_com = center_of_mass - self.position
            if vec_to_com.norm() > 0:
                vec_to_com = (vec_to_com / vec_to_com.norm()) * self.max_speed
            steering = vec_to_com - self.velocity
            if steering.norm() > self.max_force:
                steering = (steering / steering.norm()) * self.max_force
        return steering

    # Proprietatea de a schima directia pentru a evita ciocnirea cu alti asteroizi
    def separation(self, boids):
        steering = IVector(array.array("f", [0, 0]))
        total = 0
        avg_vector = IVector(array.array("f", [0, 0]))
        for boid in boids:
            distance = (boid.position - self.position).norm()
            if self.position != boid.position and distance < self.perception:
                diff = self.position - boid.position
                diff /= distance
                avg_vector += diff
                total += 1
        if total > 0:
            avg_vector /= total
            avg_vector = IVector(avg_vector.get_values())
            if steering.norm() > 0:
                avg_vector = (avg_vector / steering.norm()) * self.max_speed
            steering = avg_vector - self.velocity
            if steering.norm() > self.max_force:
                steering = (steering / steering.norm()) * self.max_force
        return steering

    def calm_flocking(self, boids):
        alignment = self.align(boids)
        cohesion = self.cohesion(boids)
        separation = self.separation(boids)
        return alignment * 0.04 + cohesion * 0.02 + separation * 0.02


boids = []


MAX_WIDTH = 320
MAX_HEIGHT = 240
text_msg = ""


def setup():
    size(MAX_WIDTH, MAX_HEIGHT)
    no_stroke()
    background(204)


def draw():
    background(204)
    for i in range(len(boids)):
        boids[i].update()
        boids[i].edges()
        boids[i].show()

        if text_msg == "Separation":
            separation = boids[i].separation(boids)
            boids[i].acceleration += separation * 0.03
        elif text_msg == "Alignment":
            alignment = boids[i].align(boids)
            boids[i].acceleration += alignment * 0.03
        elif text_msg == "Cohesion":
            cohesion = boids[i].cohesion(boids)
            boids[i].acceleration += cohesion * 0.03
        elif text_msg == "Calm flocking":
            calm_flocking = boids[i].calm_flocking(boids)
            boids[i].acceleration += calm_flocking
    if mouse_is_pressed:
        if mouse_button == LEFT:
            boids.append(
                Boid(mouse_x, mouse_y, MAX_WIDTH, MAX_HEIGHT, random.randint(50, 255))
            )
        elif mouse_button == RIGHT:
            boids.clear()

    text_size = 15
    x = MAX_WIDTH - textWidth(text_msg) - 10
    y = MAX_HEIGHT - text_size - 10
    text(text_msg, x, y)


def key_pressed():
    global text_msg

    if key == "q":
        text_msg = "Separation"
    if key == "w":
        text_msg = "Alignment"
    if key == "e":
        text_msg = "Cohesion"
    if key == "r":
        text_msg = "Calm flocking"
    if key == "t":
        text_msg = ""


run(renderer="vispy")
