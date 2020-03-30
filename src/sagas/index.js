import { all } from 'redux-saga/effects';

import { onLocation } from './Location';
import { onStores } from './Stores';
import { onSearch } from './Search';

export default function* rootSaga() {
  yield all([onLocation(), onStores(), onSearch()]);
}
