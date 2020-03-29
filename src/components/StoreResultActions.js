export function hoverResult(key) {
  return {
    type: 'HOVER_RESULT',
    payload: { key }
  };
}

export function viewDetailedInfo(key) {
  return {
    type: 'VIEW_DETAILED_INFO',
    payload: { key }
  };
}
