package com.example.thrift;

import com.partners.iot.thrift.Comments;
import com.partners.iot.thrift.EventDTO;
import com.partners.iot.thrift.InvalidOperation;
import com.partners.iot.thrift.ReportService;
import org.apache.thrift.TException;
import org.apache.thrift.protocol.TBinaryProtocol;
import org.apache.thrift.protocol.TProtocol;
import org.apache.thrift.transport.TSocket;
import org.apache.thrift.transport.TTransport;
import org.apache.thrift.transport.TTransportException;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by haduart on 08/03/17.
 */
@Component
public class ThriftService {


    @Value("${thrift.server}")
    private String thriftServer;

    @Value("${thrift.port}")
    private String thriftPort;

    public String execute() {
        Integer thriftPortNumber = Integer.parseInt(this.thriftPort);
        TTransport transport = new TSocket(thriftServer, thriftPortNumber);
        try {
            transport.open();


            TProtocol protocol = new TBinaryProtocol(transport);
            ReportService.Client client = new ReportService.Client(protocol);

            List<EventDTO> thriftBeanList = new ArrayList<EventDTO>();

            EventDTO event = new EventDTO(
                    "Descripcio desde Java", "Eduard", "27/05/2016 09:44:32", 12, false, true, false, "OPERATIONEEL");

            event.addToComments(new Comments("Eduard", "6/06/2016 06:06:06", "I don't like this operation state"));

            thriftBeanList.add(event);


            String pythonResponse = client.createReport("Report1", thriftBeanList, "Summary", "Eduard");
            transport.close();

            return pythonResponse;
        } catch (TTransportException e) {
            e.printStackTrace();
        } catch (InvalidOperation invalidOperation) {
            invalidOperation.printStackTrace();
        } catch (TException e) {
            e.printStackTrace();
        }
        return "";
    }
}
