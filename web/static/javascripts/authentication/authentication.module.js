function () {
    'use strict';

    angular
	.module('tbeast.authentication', ['tbeast.authentication.controllers',
					  'tbeast.authentication.services']);

    angular
	.module('tbeast.authentication.controllers', []);

    angular
	.module('tbeast.authentication.services', ['ngCookies']);
})();