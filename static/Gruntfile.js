module.exports = function (grunt) {

    "use strict";

    // Iniciando a configuração das tarefas
    grunt.initConfig({

	  uglify: {
	    options: {
	      mangle: false
	    },
	    my_target: {
	      files: {
	        'js/all.min.js': ['js/main.js']
	      }
	    },
	   },

        watch: {
            files: "sass/*.scss",
            tasks: 'sass',
        },


	    sass: { 
	        dev: {                                // another target
	            options: {                        // dictionary of render options
	                sourceMap: true
	            },
	            files: {
	                'css/style.css': 'sass/style.scss',
	            }
	        }
	    },

        compass: {
            dist: {
                options: {
                    sassDir: 'sass',
                    cssDir: 'css',
                    outputStyle: 'compressed'
                },
            },
        },

        browser_sync: {
            files: {

                // Aplicando o recurso de Live Reload nos seguintes arquivos
                src : [
                    'css/*.css',
                    '*.html'
                ],

            },
            options: {

                // Definindo um IP manualmente
                host : "192.168.0.95",

                // Atribuíndo um diretório base
                server: {
                    baseDir: "."
                },

                // Integrando com a tarefa "watch"
                watchTask: true,

                // Sincronizando os eventos entre os dispositívos
                ghostMode: {
                    scroll: true,
                    links: true,
                    forms: true
                }
            },
        }
    });

    // Carregando os plugins
    grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-browser-sync');
	grunt.loadNpmTasks('grunt-sass');


    // Registrando tarefas customizadas
    grunt.registerTask('default', ["browser_sync", "watch"]);
};