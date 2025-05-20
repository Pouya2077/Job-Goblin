const isProd = process.env.NODE_ENV === 'production';
import purgeCss from '@fullhuman/postcss-purgecss';
import combineMediaQuery from 'postcss-combine-media-query';
import combineSelectors from 'postcss-combine-duplicated-selectors';
import autoprefixer from 'autoprefixer';
import sorter from 'css-declaration-sorter';
import nano from 'cssnano';
import path from 'path';

export default {
  plugins: isProd
    ? [
        purgeCss({
          content: [
            path.resolve(path.resolve(), './src/**/*.js'),
            path.resolve(path.resolve(), './src/**/*.jsx'),
            path.resolve(path.resolve(), './src/index.ejs'),
          ],
          keyframes: false,
        }),
        combineSelectors({ removeDuplicatedProperties: true }),
        combineMediaQuery(),
        autoprefixer(),
        sorter(),
        nano(),
      ]
    : [],
};
