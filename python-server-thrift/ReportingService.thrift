namespace java com.partners.iot.thrift

struct Comments {
    1: string user,
    2: string time,
    3: string text
}

struct EventDTO {
    1: required string description,
    2: required string user,
    3: required string ts,
    4: required i32 id,
    5: required bool starred,
    6: required bool startEvent,
    7: required bool stopEvent,
    8: required string typeName,
    9: optional list<Comments> comments
}

exception InvalidOperation {
  1: i32 whatOp,
  2: string why
}

service ReportService {
   string createReport(1:string reportName, 2:list<EventDTO> events, 3:string reportType, 4:string userName) throws (1:InvalidOperation ouch)

}
