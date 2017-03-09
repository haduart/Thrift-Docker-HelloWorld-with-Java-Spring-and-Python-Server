package com.example.api;

import com.example.thrift.ThriftService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

/**
 * Created by haduart on 08/03/17.
 */
@RestController
@RequestMapping("/hello")
public class HelloController {

    @Autowired
    ThriftService thriftService;

    @RequestMapping(method = RequestMethod.GET)
    String hello() {
        return "says hi! - " + thriftService.execute();
    }
}
