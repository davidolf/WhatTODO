/**
 * 
 */

var whatTodoApp = angular.module('WhatTODO.app.todo', []);

whatTodoApp.controller('TodoController', function($scope, $http) {
		$scope.todos = [];
		$http.get('api/todos').success(function (data) {
			angular.forEach(data, function(value) {
				var todo = {};
				todo.tag = value.tag.text;
				todo.text = value.text;
				$scope.todos.push(todo);
			});
		});
	});