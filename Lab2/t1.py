import math
import numpy as np
from p5 import *
import random
import array


class Boid:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height
        self.max_speed = 10
        self.perception = 100
        self.max_force = 1
        self.position = Vector(x, y)
        vec = array.array(
            "f", [(random.random() - 0.5) * 10, (random.random() - 0.5) * 10]
        )
        self.velocity = Vector(*vec)
        vec = array.array(
            "f", [(random.random() - 0.5) / 2, (random.random() - 0.5) / 2]
        )
        self.acceleration = Vector(*vec)

    def update(self):
        self.position += self.velocity
        self.velocity += self.acceleration  # limit
        if np.linalg.norm(self.velocity) > self.max_speed:
            self.velocity = (
                self.velocity / np.linalg.norm(self.velocity) * self.max_speed
            )
        self.acceleration = Vector(*np.zeros(2))

    def show(self, color=255):
        stroke(color)
        circle(self.position.x, self.position.y, 10)

    def edges(self):
        if self.position.x > self.width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = self.width
        if self.position.y > self.height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = self.height

    # Proprietatea de a se orienta in directia miscarii flotei
    def align(self, boids):
        steering = Vector(*np.zeros(2))
        total = 0
        avg_vec = Vector(*np.zeros(2))
        for boid in boids:
            if np.linalg.norm(boid.position - self.position) < self.perception:
                avg_vec += boid.velocity
                total += 1
        if total > 0:
            avg_vec /= total
            avg_vec = Vector(*avg_vec)
            avg_vec = (avg_vec / np.linalg.norm(avg_vec)) * self.max_speed
            steering = avg_vec - self.velocity
        return steering

    # Proprietatea de a se apropia de flota
    def cohesion(self, boids):
        steering = Vector(*np.zeros(2))
        total = 0
        center_of_mass = Vector(*np.zeros(2))
        for boid in boids:
            if np.linalg.norm(boid.position - self.position) < self.perception:
                center_of_mass += boid.position
                total += 1
        if total > 0:
            center_of_mass /= total
            center_of_mass = Vector(*center_of_mass)
            vec_to_com = center_of_mass - self.position
            if np.linalg.norm(vec_to_com) > 0:
                vec_to_com = (vec_to_com / np.linalg.norm(vec_to_com)) * self.max_speed
            steering = vec_to_com - self.velocity
            if np.linalg.norm(steering) > self.max_force:
                steering = (steering / np.linalg.norm(steering)) * self.max_force
        return steering

    # Proprietatea de a schima directia pentru a evita ciocnirea cu alti asteroizi
    def separation(self, boids):
        steering = Vector(*np.zeros(2))
        total = 0
        avg_vector = Vector(*np.zeros(2))
        for boid in boids:
            distance = np.linalg.norm(boid.position - self.position)
            if self.position != boid.position and distance < self.perception:
                diff = self.position - boid.position
                diff /= distance
                avg_vector += diff
                total += 1
        if total > 0:
            avg_vector /= total
            avg_vector = Vector(*avg_vector)
            if np.linalg.norm(steering) > 0:
                avg_vector = (avg_vector / np.linalg.norm(steering)) * self.max_speed
            steering = avg_vector - self.velocity
            if np.linalg.norm(steering) > self.max_force:
                steering = (steering / np.linalg.norm(steering)) * self.max_force
        return steering

    def calm_flocking(self, boids):
        alignment = self.align(boids)
        cohesion = self.cohesion(boids)
        separation = self.separation(boids)
        return alignment * 0.02 + cohesion * 0.02 + separation * 0.02


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
        boids[i].show(50 if i == 0 else 255)

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
            boids.append(Boid(mouse_x, mouse_y, MAX_WIDTH, MAX_HEIGHT))
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
