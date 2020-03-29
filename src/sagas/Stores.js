import { call, put, takeEvery } from 'redux-saga/effects';
import { storesApi } from './API';

export function* onStores() {
  yield takeEvery('SEARCH_API_STORES', fetchStores);
}

export function* fetchStores(action) {
  try {
    yield put({ type: 'SEARCH_STORES_PENDING', payload: {} });

    const stores = yield call(storesApi, action.payload);

    yield put({
      type: 'SEARCH_STORES_SUCCESS',
      payload: { stores: stores.data.stores }
    });
  } catch (e) {
    yield put({ type: 'SEARCH_SET_ERROR', payload: { error: e.message } });
  }
}
