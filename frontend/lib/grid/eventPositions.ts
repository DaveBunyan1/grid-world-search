import { SearchEvent, SearchEventType } from "@/types/api";

export function eventPositions(events: SearchEvent[], type: SearchEventType) {
  return new Set(
    events
      .filter((event) => event.event_type === type)
      .map((event) => `${event.node.row}-${event.node.col}`),
  );
}
