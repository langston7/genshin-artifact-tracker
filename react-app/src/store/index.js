import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import artifactReducer from './artifacts';
import chartDataReducer from './chart_data';
import session from './session'
import userArtifactReducer from './user_artifacts';

const rootReducer = combineReducers({
  session,
  artifacts: artifactReducer,
  userArtifacts: userArtifactReducer,
  chartData: chartDataReducer
});


let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
