# -*- coding: utf-8 -*-

from Odoo import models, fields

class SchoolSubject (models.Model):
     _name = 'school.subject'

     name = fields.Char(string='Nombre', required=True)
  
     credits = fields.Integer(string='Número de créditos de la asignatura')

     max_students = fields.Integer(string='Cantidad máxima de estudiantes de la asignatura')

     active = fields.Boolean('La asignatura está activa?', default=False)

     student_ids = fields.Many2many('school.student', 'subject_ids', string='Estudiantes')

     teacher_id = fields.Many2one('school.teacher', string='Profesores')


class SchoolStudent (models.Model):
     _name = 'school.student'

     name = fields.Char(string='Nombre del estudiante', required=True)

     birth_date = fields.Date(string='Fecha de nacimiento del estudiante')

     age = fields.Integer(string='Edad del estudiante')

     final_exam_grade = fields.Float(string='Calificación del estudiante en el examen final')

     subject_ids = fields.Many2many('school.subject','student_ids', string='Asignaturas')



class SchoolTeacher (models.Model):
     _name = 'school.teacher'

     name = fields.Char(string='Nombre del profesor', required=True)

     profile = fields.Text(string='Perfil del profesor')

     subject_ids = fields.One2many('school.subject', 'teacher_id', string='Asignaturas')
