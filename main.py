# -*- coding:utf-8 -*-
from flask import Flask, render_template, request, flash,  jsonify
import json
from utils.query import query

# 创建flask对象
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/course_discussion', methods=['GET', 'POST'])
def course_discussion():
    return render_template('course_discussion.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/news_center', methods=['GET', 'POST'])
def news_center():
    return render_template('news_center.html')


@app.route('/personal_information', methods=['GET', 'POST'])
def personal_information():
    return render_template('personal_information.html')


@app.route('/train_plan', methods=['GET', 'POST'])
def train_plan():
    data = {'name': '数据转换成功', 'children': [{'name': '123123123', 'children': [{'name': 'FlareVis', 'value': 4116, 'itemStyle': {'borderColor': 'red'}}]}, {'name': 'scale', 'children': [{'name': 'TimeScale', 'value': 5833, 'categories': 1, 'itemStyle': {'borderColor': 'red'}}]}, {'name': 'display', 'children': [{'name': 'DirtySprite', 'value': 8833, 'itemStyle': {'borderColor': 'red'}}]}]}
    return render_template('train_plan.html')

@app.route('/get_info', methods=['GET', 'POST'])
def get_info():
    data = {'name': '数据转换成功', 'children': [{'name': '123123123', 'children': [{'name': 'FlareVis', 'value': 4116, 'itemStyle': {'borderColor': 'red'}}]}, {'name': 'scale', 'children': [{'name': 'TimeScale', 'value': 5833, 'categories': 1, 'itemStyle': {'borderColor': 'red'}}]}, {'name': 'display', 'children': [{'name': 'DirtySprite', 'value': 8833, 'itemStyle': {'borderColor': 'red'}}]}]}
    print(data)
    return jsonify(data)

@app.route('/submit_train_plan', methods=['GET', 'POST'])
def submit_train_place():
    train_plan = request.get_json(force=True)
    train_plan['name'] = "数据转换成功"
    print(train_plan)
    return jsonify(train_plan)


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True)


