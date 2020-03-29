import { all } from 'redux-saga/effects';

import { onLocation } from './Location';
import { onStores } from './Stores';

export default function* rootSaga() {
  yield all([onLocation(), onStores()]);
}
