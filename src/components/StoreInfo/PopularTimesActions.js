export function hoverBar(hour, day) {
  return {
    type: 'UPDATE_POPULAR_TIME',
    payload: { hour: hour, day: day }
  };
}
