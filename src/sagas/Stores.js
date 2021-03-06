import { call, put, takeEvery } from 'redux-saga/effects';
import { storesApi } from './API';

export function* onStores() {
  yield takeEvery('SEARCH_API_STORES', fetchStores);
}

export function* fetchStores(action) {
  try {
    yield put({ type: 'SEARCH_STORES_PENDING', payload: {} });

    let stores = yield call(storesApi, action.payload);
    stores = stores.data.stores.map((store, index) => {
      if ('populartimes' in store.popular) {
        if (store.popular.current_popularity < 0) {
          const currentTime = new Date();
          const currentDay = (currentTime.getDay() + 6) % 7;
          const currentMins = currentTime.getMinutes();
          const currentHour = currentTime.getHours();

          const byHour = store.popular.populartimes[6].data;
          store.popular.current_popularity =
            ((60.0 - currentMins) / 60.0) * byHour[currentHour % 24] +
            (currentMins / 60.0) *
              store.popular.populartimes[(currentDay + 1) % 7].data[0];
        }
      } else {
        store.popular.current_popularity = 0;
      }
      store.safety =
        ((store.current_speed / store.free_flow_speed) * 4 +
          1 +
          (((100 - store.popular.current_popularity) / 100) * 4 + 1)) /
        2;
      return store;
    });

    yield put({
      type: 'SEARCH_STORES_SUCCESS',
      payload: { stores: stores }
    });
  } catch (e) {
    yield put({ type: 'SEARCH_SET_ERROR', payload: { error: e.message } });
  }
}
