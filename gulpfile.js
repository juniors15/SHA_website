'use strict';

const gulp = require('gulp'); 
const babel = require('gulp-babel');
const sourcemaps = require('gulp-sourcemaps');
const sass = require('gulp-sass'); 
const imagemin = require('gulp-imagemin');
const server = require('gulp-server-livereload'); 
const injectPartials = require('gulp-inject-partials'); 
const autoprefixer = require('gulp-autoprefixer');
const minifyCss = require('gulp-minify-css');
const rename = require('gulp-rename');

gulp.task('default', ['bake', 'sass', 'imagemin', 'watch']);
gulp.task('serve', ['webserver', 'default']); 
   
gulp.task('bake', function () { 
    return gulp.src('./src/*.html')
    .pipe(injectPartials({
        start: '<!--(bake {{path}})', 
        end: '-->',
        removeTags: true
    }))
    .pipe(gulp.dest('./public')); 
});

gulp.task('sass', function () {
  return gulp.src('./src/css/sass/style.scss')
    .pipe(sourcemaps.init())
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('./public/css'))
    .pipe(minifyCss({
        keepSpecialComments: 0
    }))
    .pipe(rename({ extname: '.min.css' }))
    .pipe(gulp.dest('./public/css'))
}); 

gulp.task('imagemin', () =>
    gulp.src('src/images/**/*.{png,jpg,gif}')
    .pipe(imagemin())
    .pipe(gulp.dest('public/images'))
); 

gulp.task('watch', [], function() {
    gulp.watch('**/*.scss', ['sass']);
    gulp.watch('./src/images/*', ['imagemin']); 
    gulp.watch('./src/*.html', ['bake']); 
});

gulp.task('webserver', function() {
  gulp.src('./public')
    .pipe(server({
      livereload: true,
      directoryListing: false,
      open: true,
      port: 9002,
      host: '0.0.0.0', 
    }));
});