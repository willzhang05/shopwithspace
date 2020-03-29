import { call, put, takeEvery } from 'redux-saga/effects';
import { locationApi } from './API';

export function* onLocation() {
  yield takeEvery('SEARCH_API_LOCATION', fetchLocation);
}

export function* fetchLocation(action) {
  try {
    yield put({ type: 'SEARCH_LOCATION_PENDING', payload: {} });

    const location = yield call(locationApi, action.payload);

    yield put({
      type: 'SEARCH_LOCATION_SUCCESS',
      payload: { location: location }
    });
  } catch (e) {
    yield put({ type: 'SEARCH_SET_ERROR', payload: { error: e.message } });
  }
}
